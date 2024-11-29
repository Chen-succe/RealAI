from http.server import SimpleHTTPRequestHandler, HTTPServer

def run():
    server_address = ('', 8080)
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    print('server start at http ://lcoalhost:8080/')
    httpd.serve_forever()

if __name__ == '__main__':
    run()