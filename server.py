# importing necessary libraries
from http.server import BaseHTTPRequestHandler, HTTPServer

# defining host and ports for easy reuse
HOST = "127.0.0.1"
PORT = 8000

# instantiate the server
# HTTPServer(("host", port), handler_class)
server = HTTPServer((HOST, PORT), BaseHTTPRequestHandler)

# print so we now server is running
print(f"listening on http://{HOST}:{PORT}...")

# loop to keep listening
server.serve_forever()
