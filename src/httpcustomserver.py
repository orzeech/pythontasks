from http.server import BaseHTTPRequestHandler, HTTPServer


class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        message = "{\"students\":[\"Anna\",\"Marcin\",\"Karol\"]}"

        self.protocol_version = "HTTP/1.1"
        self.send_response(200)
        self.send_header("Content-Length", len(message))
        self.send_header("Content-Type", "application/json")
        self.end_headers()

        self.wfile.write(bytes(message, "utf8"))
        return


def run():
    server = ('', 80)
    httpd = HTTPServer(server, RequestHandler)
    httpd.serve_forever()


if __name__ == '__main__':
    run()
