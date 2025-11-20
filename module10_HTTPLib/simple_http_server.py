from http.server import BaseHTTPRequestHandler, HTTPServer


class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"Hello from server!")

        message = "<h1>Hello from Python HTTP Server!</h1>"
        self.wfile.write(message.encode("utf-8"))


def run():
    server = HTTPServer(("localhost", 8080), SimpleHandler)
    print("Server running on http://localhost:8080")
    server.serve_forever()



if __name__ == "__main__":
    run()
