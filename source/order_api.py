from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import database


class OrderHandler(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/json')
        self.end_headers()

    def do_GET(self):
        self._set_headers()

        orders = database.get_all_orders()

        jd = json.dumps(orders)

        self.wfile.write(jd.encode('utf-8'))

    def do_POST(self):
        content_length = int(self.headers["Content-length"])
        data = json.loads(self.rfile.read(content_length))

        round_id = data["round_id"]
        person = data["person"]
        drink = data["drink"]

        database.add_order(round_id, person, drink)

        self.send_response(201)
        self.end_headers()


if __name__ == "__main__":
    server_address = ('', 8080)
    httpd = HTTPServer(server_address, OrderHandler)
    print("Starting server...")

    httpd.serve_forever()
