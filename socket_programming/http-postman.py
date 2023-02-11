import json
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

    # JSON data 수신
    request_data = client_connection.recv(1028)

    # TODO: JSON data로 파싱하려 했으나 에러가 남
    if request_data:
        try:
            request_data_str = request_data.decode('utf-8')
            request = json.loads(request_data_str)
        except json.decoder.JSONDecodeError:
            request = {}
    else:
        request = {}

    print(request)

    # 송신할 딕셔너리 형태의 데이터를 JSON으로 직렬화
    sample_data = {"success": "Hello World"}
    json_response = json.dumps(sample_data)

    # JSON 데이터 송신
    http_response = (
        "HTTP/1.1 200 OK\r\n"
        "Content-Type: application/json\r\n"
        f"Content-Length: {len(json_response)}\r\n"
        "\r\n"
        f"{json_response}"
    )

    client_connection.sendall(http_response.encode('utf-8'))

    client_connection.close()

