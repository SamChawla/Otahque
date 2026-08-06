# illustration_only/minimal_web_server.py
# NOTE: Educational illustration only. Do not use in production.

import socket


def handle_request(raw_request: bytes) -> bytes:
    """Parse an HTTP request and return an HTTP response."""
    request_text = raw_request.decode("utf-8")
    lines = request_text.split("\r\n")
    method, path, _ = lines[0].split(" ")

    if method == "GET" and path == "/events/":
        body = "<html><body><h1>Events</h1></body></html>"
        status = "200 OK"
    else:
        body = "<html><body><h1>404 Not Found</h1></body></html>"
        status = "404 Not Found"

    response = (
        f"HTTP/1.1 {status}\r\n"
        f"Content-Type: text/html\r\n"
        f"Content-Length: {len(body)}\r\n"
        f"\r\n"
        f"{body}"
    )
    return response.encode("utf-8")


def run_server(host: str = "127.0.0.1", port: int = 8000) -> None:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind((host, port))
        server.listen(1)
        print(f"Listening on http://{host}:{port}")
        while True:
            conn, _ = server.accept()
            with conn:
                data = conn.recv(4096)
                response = handle_request(data)
                conn.sendall(response)


if __name__ == "__main__":
    run_server()
