# import websocket
#
# def on_message(ws, message):
#     print(f"收到服务端消息: {message}")
#
# def on_open(ws):
#     print("连接成功，发送消息...")
#     ws.send("你好，服务端！")
#
# def on_close(ws, close_status_code, close_msg):
#     print("连接关闭")
#
# # 连接服务端
# ws = websocket.WebSocketApp(
#     "ws://localhost:8765",
#     on_message=on_message,
#     on_open=on_open,
#     on_close=on_close
# )
#
# ws.run_forever()
#
import asyncio
import websockets

async def hello():
    async with websockets.connect("ws://localhost:8765") as websocket:
        await websocket.send("你好，服务端！")
        reply = await websocket.recv()
        print(f"收到: {reply}")

asyncio.run(hello())
