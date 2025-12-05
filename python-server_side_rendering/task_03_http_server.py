import http.server
import json

class SimpleHTTPRequestHandler(http.server.BaseHTTPRequestHandler):
    """
    A simple HTTP request handler that handles GET requests
    and serves JSON data or plain text based on the endpoint.
    """

    def do_GET(self):
        """
        Handle GET requests.
        """
        # 1. Handle the root endpoint "/"
        if self.path == '/':
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        # 2. Handle the "/data" endpoint (Serving JSON)
        elif self.path == '/data':
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            
            # Create the dictionary and convert to JSON string
            data = {"name": "John", "age": 30, "city": "New York"}
            json_response = json.dumps(data)
            
            # Send the JSON string as bytes
            self.wfile.write(json_response.encode('utf-8'))

        # 3. Handle the "/status" endpoint (Check API status)
        elif self.path == '/status':
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK")

        # 4. Handle the "/info" endpoint (From Expected Output requirements)
        elif self.path == '/info':
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            info_data = {"version": "1.0", "description": "A simple API built with http.server"}
            self.wfile.write(json.dumps(info_data).encode('utf-8'))

        # 5. Handle undefined endpoints (404 Not Found)
        else:
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Endpoint not found")

def run(server_class=http.server.HTTPServer, handler_class=SimpleHTTPRequestHandler, port=8000):
    """
    Starts the HTTP Server.
    """
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting server on port {port}...")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print("Server stopped.")

if __name__ == '__main__':
    run()
