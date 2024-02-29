from http.server import HTTPServer, BaseHTTPRequestHandler
import ssl

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'Success!')

    def do_POST(self):
        self.send_response(200)
        self.end_headers()
        print(self.rfile.read(int(self.headers['content-length'])).decode('utf-8'))
        self.wfile.write(b'Success')

def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler):
    server_address = ('', 443)
    httpd = server_class(server_address, handler_class)
    httpd.socket = ssl.wrap_socket(httpd.socket,
                                   server_side=True,
                                   certfile='cert.pem',
                                   keyfile='key.pem',
                                   ssl_version=ssl.PROTOCOL_TLS)
    print(f'Starting httpsd server on port 443')
    httpd.serve_forever()

if __name__ == '__main__':
    run()
~          
