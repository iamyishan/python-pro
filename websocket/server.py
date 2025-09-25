import asyncio
import websockets

# handler 只需要接收 websocket 参数
async def handler(websocket):
    print(f"客户端已连接")
    try:
        async for message in websocket:
            print(f"收到客户端消息: {message}")
            reply = f"服务端回应: {message}"
            await websocket.send(reply)
    except websockets.exceptions.ConnectionClosed:
        print("客户端已断开")

async def main():
    async with websockets.serve(handler, "localhost", 8765):
        print("WebSocket 服务已启动，端口 8765")
        await asyncio.Future()  # 保持运行

asyncio.run(main())
