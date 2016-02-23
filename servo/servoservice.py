import BaseHTTPServer
import json

class ServoHandler(BaseHTTPServer.BaseHTTPRequestHandler) :
    def go_HEAD(s):
        s.send_response(200)
        s.send_header("Content-type", "text")
        s.end_headers()
    def do_POST(self):
        print(self.__dict__)
        length = int(self.headers["Content-Length"])
        post_data = self.rfile.read(length)
        query = json.loads(post_data)
        self.send_response(200)
        self.send_header("Content-type", "text")
        self.end_headers()
        self.wfile.write("hello\n")
        print("done")

server = BaseHTTPServer.HTTPServer(("localhost",8080), ServoHandler)

try :
    server.serve_forever()
except KeyboardInterrupt :
    pass
server.server_close()
print("goodbye")
