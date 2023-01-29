import socket

# tcp socket 객체 생성
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 127.0.0.1:7777에 접속한다.
client_socket.connect(('127.0.0.1', 7777))

# 서버에게 보낼 메시지를 입력하고 전송한다.
message = input("메시지를 입력하세요.:")
client_socket.send(message.encode('utf-8'))

# receive a response from the server
response = client_socket.recv(1024).decode()

# 서버에서 보낸 응답 값을 출력 한다.
print(f"서버 응답 값: {response}")

# 소켓을 종료한다.
client_socket.close()
