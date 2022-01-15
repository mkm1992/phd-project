from http.server import BaseHTTPRequestHandler, HTTPServer

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()

        message = "Hello, World! Here is a GET response"
        self.wfile.write(bytes(message, "utf8"))

    def do_POST(self):
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()

        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)

        message = "Hello, World! Here is a POST response to: " + post_data.decode('utf-8')
        sp = post_data.decode('utf-8').split('=')
        print(sp)
        self.wfile.write(bytes(message, "utf8"))

with HTTPServer(('', 8001), handler) as server:
    server.serve_forever()

# curl -d "name=hossein" http://localhost:8000
# curl http://localhost:8000
