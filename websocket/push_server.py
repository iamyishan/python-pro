import asyncio
import websockets
import json
import time

connected_clients = set()

async def handler(websocket):
    connected_clients.add(websocket)
    print(f"客户端已连接，当前连接数: {len(connected_clients)}")
    
    try:
        await websocket.wait_closed()
    except websockets.exceptions.ConnectionClosed:
        pass
    finally:
        connected_clients.remove(websocket)
        print(f"客户端已断开，当前连接数: {len(connected_clients)}")

async def push_data():
    """定时推送数据到所有客户端"""
    global connected_clients
    counter = 0
    while True:
        if connected_clients:
            counter += 1
            data = {
                "type": "push",
                "message": f"服务端推送消息 #{counter}",
                "timestamp": time.time()
            }
            
            # 向所有连接的客户端推送数据
            disconnected = set()
            for client in connected_clients:
                try:
                    await client.send(json.dumps(data))
                except websockets.exceptions.ConnectionClosed:
                    disconnected.add(client)
            
            # 清理断开的连接
            connected_clients -= disconnected
            
        await asyncio.sleep(2)  # 每2秒推送一次

async def main():
    # 启动推送任务
    push_task = asyncio.create_task(push_data())
    
    async with websockets.serve(handler, "localhost", 8766):
        print("推流服务已启动，端口 8766")
        try:
            await asyncio.gather(push_task)
        except KeyboardInterrupt:
            push_task.cancel()

asyncio.run(main())