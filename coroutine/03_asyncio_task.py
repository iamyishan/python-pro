import asyncio
import time

'''
任务对象：
    任务对象是对协程的进一步封装，用于管理协程的执行和状态。
    任务对象可以被添加到事件循环中，由事件循环来调度和执行。
    任务对象有一个done()方法，用于判断任务是否完成，返回True或False。
    任务对象有一个result()方法，用于获取任务的返回值。
    任务对象有一个add_done_callback()方法，用于添加一个回调函数，当任务完成时会调用回调函数,而不必等待所有任务完成才执行。
'''


def callback(task):
    print(f"callback {task.result()} completed")

async def task(i):
    print(f"Task {i} started")
    await asyncio.sleep(i)  # 模拟任务的耗时操作
    print(f"Task {i} finished")
    return i
t1=time.time()

# (1)构建事件循环对象
loop = asyncio.get_event_loop()

# (2)创建任务对象
tasks = [asyncio.ensure_future(task(i)) for i in range(3)]
for task in tasks:
    task.add_done_callback(callback)
# (3)运行事件循环，直到所有任务完成
loop.run_until_complete(asyncio.wait(tasks))


for task in tasks:
   print(task.result())

print(f"All tasks completed in {time.time()-t1} seconds")