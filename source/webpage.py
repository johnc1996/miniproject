from http.server import HTTPServer, BaseHTTPRequestHandler
import database


def get_all_people():
    sql_query = """
    SELECT name FROM tb_People
    """
    return database.db_return_rows(sql_query)


def render_drinks(drinks):
    drinks_html = ""
    for drink in drinks:
        drinks_html += f'<li>{drink}</li>'

    return drinks_html


def render_people(people):
    people_html = ""
    for person_row in people:
        people_html += f'<li>{person_row[0]}</li>'
    return people_html


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Tell the client we're about to send HTML content in our HTTP payload
        self.send_response(200)
        self.send_header('Content-Type', 'text/html')
        self.end_headers()

        people = get_all_people()

        # Produce the HTML
        html_document = f"""
<!doctype html>
<html>
    <body>
        <p>People in database:</p>
        <ul>
            {render_people(people)}
        </ul>
    </body>
</html>
"""
        # Render and send response
        self.wfile.write(html_document.encode('utf-8'))


if __name__ == "__main__":
    server_address = ('', 8080)
    httpd = HTTPServer(server_address, Handler)
    print("Starting server")
    httpd.serve_forever()
