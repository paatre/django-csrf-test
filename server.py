import http.server
import socketserver


class MyRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers.get('Content-Length', 0))
        post_data = self.rfile.read(content_length)

        print("Received POST data:", post_data.decode('utf-8'))

        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(b"POST received")


with socketserver.TCPServer(("", 8001), MyRequestHandler) as httpd:
    print("Serving on port 8001")
    httpd.serve_forever()
