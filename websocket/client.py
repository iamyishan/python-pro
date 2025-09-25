import asyncio
import websockets
import json
import threading


async def send_messages(websocket, username):
    """发送消息的协程"""
    while True:
        message = input("请输入消息（输入exit退出）: ")
        if message.lower() == "exit":
            break
        await websocket.send(json.dumps({
            "sender": username,
            "message": message
        }))


async def receive_messages(websocket):
    """接收消息的协程"""
    while True:
        message = await websocket.recv()
        data = json.loads(message)
        print(f"\n收到 {data['sender']} 的消息: {data['message']}")
        print("请输入消息（输入exit退出）: ", end="", flush=True)


async def main():
    username = input("请输入你的用户名: ")
    async with websockets.connect("ws://localhost:8765") as websocket:
        # 启动接收消息的线程
        receive_task = asyncio.create_task(receive_messages(websocket))

        # 发送消息
        await send_messages(websocket, username)

        # 取消接收任务
        receive_task.cancel()
        try:
            await receive_task
        except asyncio.CancelledError:
            pass


asyncio.run(main())