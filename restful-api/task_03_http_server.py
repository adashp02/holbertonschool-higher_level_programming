#!/usr/bin/python3
"""Simple API - Python web server"""
import http.server
import json
import socketserver

PORT = 8000

class My_Handler(http.server.BaseHTTPRequestHandler):
    """creating a subclass of BaseHTTPRequestHandler"""

    def do_GET(self):
        """method to handle GET requests"""

        #base access
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'tesxt/plain')
            self.end_headers()
            self.wfile.write('Hello, this is a simple API!'.encode())

        #in case /data endpoint is accessed
        elif self.path == '/data':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            data = {
                "name": "John",
                "age": 30,
                "city": "New York"
            }
            #convert data as JSON
            self.wfile.write(json.dumps(data).encode('utf-8'))

        #in case /status endpoint accessed
        elif self.path == '/status':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write('OK'.encode('utf-8'))

        #if /info accessed
        elif self.path == '/info':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            data = {
                "version": "1.0",
                "description": "A simple API built with http.server"
            }
            self.wfile.write(json.dumps(data).encode('utf-8'))

        #in case any other endpoint reached - error 404
        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write('Endpoint not found'.encode())

"""initializing the server using socketserver"""

with socketserver.TCPServer(("", PORT), My_Handler) as httpd:
    print(f"Serving at port {PORT}")
    httpd.serve_forever()


