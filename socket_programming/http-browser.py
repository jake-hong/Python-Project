import socket

# host, port 변수 설정
HOST, PORT = '127.0.0.1', 7777

# tcp socket 객체 생성
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 소켓 옵션 값 설정 - 이미 사용 중인 주소 바인딩 허용
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# 바인딩
server_socket.bind((HOST, PORT))

# 요청 대기
server_socket.listen(1)
print(f"Serving HTTP on port {PORT}...")

while True:
    client_connection, client_address = server_socket.accept()
    request = client_connection.recv(1024).decode('utf-8')
    print(request)

    http_response = b"""
HTTP/1.1 200 OK

<html>
    <head>
        <title>Hello, World!</title>
    </head>
    <body>
        <h1>Hello, World!</h1>
    </body>
</html>
    """
    client_connection.sendall(http_response)
    client_connection.close()

