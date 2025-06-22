import asyncio
import time

'''
任务对象：
    任务对象是对协程的进一步封装，用于管理协程的执行和状态。
    任务对象可以被添加到事件循环中，由事件循环来调度和执行。
    asyncio.ensure_future()函数可以将协程转换为任务对象。
    asyncio.wait()函数可以将任务对象列表转换为一个任务对象，用于等待所有任务完成。
'''

async def task(i):
    print(f"Task {i} started")
    await asyncio.sleep(i)  # 模拟任务的耗时操作
    print(f"Task {i} finished")
t1=time.time()
# (1)构建事件循环对象
loop = asyncio.get_event_loop()

# (2)创建任务对象
tasks = [asyncio.ensure_future(task(i)) for i in range(3)]

# (3)运行事件循环，直到所有任务完成
loop.run_until_complete(asyncio.wait(tasks))

print(f"All tasks completed in {time.time()-t1} seconds")