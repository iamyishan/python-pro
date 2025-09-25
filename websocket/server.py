import asyncio
import websockets
import json

# 存储所有连接的客户端
connected_clients = set()


# 移除path参数，适配新版本websockets库
async def handle_client(websocket):
    # 将新连接的客户端添加到集合中
    connected_clients.add(websocket)
    try:
        async for message in websocket:
            # 解析收到的JSON消息
            data = json.loads(message)
            print(f"收到消息: {data}")

            # 广播消息给所有连接的客户端
            for client in connected_clients:
                if client != websocket:  # 不发送给自己
                    await client.send(json.dumps({
                        "type": "broadcast",
                        "message": data["message"],
                        "sender": data["sender"]
                    }))
    finally:
        # 客户端断开连接时从集合中移除
        connected_clients.remove(websocket)


async def main():
    # 启动WebSocket服务器，不再需要指定path参数
    async with websockets.serve(handle_client, "localhost", 8765):
        await asyncio.Future()  # 保持服务器运行


if __name__ == "__main__":
    asyncio.run(main())
