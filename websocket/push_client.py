import asyncio
import websockets
import json

async def client():
    async with websockets.connect("ws://localhost:8766") as websocket:
        print("已连接到推流服务器")
        
        try:
            async for message in websocket: # async for 循环会持续监听 WebSocket 连接
                data = json.loads(message)
                print(f"收到推送: {data['message']} (时间: {data['timestamp']})")
        except websockets.exceptions.ConnectionClosed:
            print("连接已断开")

asyncio.run(client())