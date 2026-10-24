Imports...
```
standard library
└── http/                          ← package
    └── server.py                  ← module
        ├── HTTPServer             ← class
        └── BaseHTTPRequestHandler ← class
```

- The server is a program that listens for traffic.

- The server listens on a host/ip and port
  - 127.0.0.1 would be local host
  - 0.0.0.0 for all traffic on network
  - ports range from 0 - 65535
  - IP is a machine's address
  - Port is a program's address
  - This allows us to target a specific program on a specific machine

- Handlers handle requests
  - Handler will have a matching do_ method for the HTTP requests
    - do_GET, do_POST, etc
  - If no handler, then 501 error.



