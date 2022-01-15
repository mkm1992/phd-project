"""
HTTP Request
"""
from http.server import BaseHTTPRequestHandler, HTTPServer
import logging
import xml.etree.ElementTree as ET
import json


class S(BaseHTTPRequestHandler):

    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        logging.info("GET request,\nPath: %s\nHeaders:\n%s\n", str(self.path), str(self.headers))
        self._set_response()
        a = str(self.path)
        str1 =  str(a[1:])
        print(str1)
        f = open('city.json',)
        data = json.load(f)
        print(data[str1])


        self.wfile.write("GET request for me {}".format(str(data[str1])).encode('utf-8'))

    def do_POST(self):
        content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
        post_data = self.rfile.read(content_length) # <--- Gets the data itself
        logging.info("POST request for me ,\nPath: %s\nHeaders:\n%s\n\nBody:\n%s\n",
                str(self.path), str(self.headers), post_data.decode('utf-8'))
        a = str(self.path)
        str1 =  str(a[1:])
        print(str1)
        f = open('city.json',)
        data = json.load(f)
        print(data[str1])
        dict_sample = dict({str1:data[str1]})
        print(json.dumps(dict_sample))
        self._set_response()
        self.wfile.write("POST request for {}".format(json.dumps(dict_sample)).encode('utf-8'))

def run(server_class=HTTPServer, handler_class=S, port=8080):
    logging.basicConfig(level=logging.INFO)
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    logging.info('Starting httpd...\n')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    logging.info('Stopping httpd...\n')

if __name__ == '__main__':
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()