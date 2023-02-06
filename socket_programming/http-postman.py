import asyncio
import json
import websockets


# webSocket 연결에 대한 요청을 처리하는 함수
async def handle_request(websocket):
    while True:
        # 요청 대기
        message = await websocket.recv(1024)
        print("Received message:", message)

        # json으로 직렬화 하여 응답
        response = {'message': 'Hello, World!'}
        await websocket.send(json.dumps(response))

# host, port 변수 설정
HOST, PORT = '127.0.0.1', 7777

# websockets 모듈을 통해 server 생성
start_server = websockets.serve(handle_request, HOST, PORT)
print(f"Serving HTTP on port {PORT}...")

# 비동기 이벤트 루프 시작 및 대기
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()

