import asyncio
import time

def callback(task):
    print(f"callback {task.result()} completed")

async def task(i):
    print(f"Task {i} started")
    await asyncio.sleep(i)  # 模拟任务的耗时操作
    print(f"Task {i} finished")
    return i**2


async def main():
    """
    主协程，同时运行多个倒计时任务
    """
    # 创建3个倒计时任务
    tasks = [asyncio.create_task(task(i)) for i in range(3)]
    for t in tasks:
        t.add_done_callback(callback)

    ret =await asyncio.gather(*tasks)
    print(ret)

if __name__ == "__main__":

    t1=time.time()
    asyncio.run(main())
    print(f"All tasks completed in {time.time()-t1} seconds")