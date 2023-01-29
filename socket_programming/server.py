import socket

# tcp socket 객체 생성
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 127.0.0.1:7777에 바인딩
server_socket.bind(('127.0.0.1', 7777))

# 상대방의 요청을 기다린다.
server_socket.listen(1)

# 상대방의 접속을 수락한다.
connection_socket, address = server_socket.accept()

# 상대방으로 부터 받은 메시지 디코드 후 수신
message = connection_socket.recv(1024).decode()

# 클라이언트에게 받은 메시지에 느낌표 2개를 붙여서 클라이언트에게 전송
connection_socket.send(f"{message}!!".encode())

# 소켓을 모두 종료한다.
connection_socket.close()
server_socket.close()

