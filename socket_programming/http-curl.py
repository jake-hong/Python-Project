import socket

# tcp socket 객체 생성
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 소켓 옵션 값 설정 - 이미 사용 중인 주소 바인딩 허용
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# host, port 변수 설정
HOST, PORT = '127.0.0.1', 7777

# 바인딩
server_socket.bind((HOST, PORT))

# 요청 대기
server_socket.listen(1)
print(f"Serving HTTP on port {PORT}...")


while True:
    client_socket, client_address = server_socket.accept()
    request = client_socket.recv(1024).decode()
    print("Requested data:", request)

    # client에게 응답
    http_response = f"HTTP/1.1 200 OK \n\n안녕하세요\n"
    client_socket.sendall(http_response.encode('utf-8'))

    # Close the client socket
    client_socket.close()
