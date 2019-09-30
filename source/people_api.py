from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import database


class PersonHandler(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/json')
        self.end_headers()

    def do_GET(self):
        self._set_headers()

        people_names = database.get_people_names()
        jd = json.dumps(people_names)

        self.wfile.write(jd.encode('utf-8'))

    def do_POST(self):
        content_length = int(self.headers["Content-length"])
        data = json.loads(self.rfile.read(content_length))

        first_name = data["first_name"]
        database.add_to_people(first_name)

        self.send_response(201)
        self.end_headers()


if __name__ == "__main__":
    server_address = ('', 8080)
    httpd = HTTPServer(server_address, PersonHandler)
    print("Starting server...")

    httpd.serve_forever()
