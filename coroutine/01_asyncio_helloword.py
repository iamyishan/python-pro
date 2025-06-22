import asyncio

'''
协程对象：
    协程对象是一个特殊的函数，它可以在执行过程中暂停和恢复。
    协程对象可以被创建和调用，但是它不会立即执行，而是返回一个协程对象。
    协程对象可以被添加到事件循环中，由事件循环来调度和执行。
    协程对象可以通过await关键字来暂停和恢复执行。
    协程对象可以通过async关键字来定义。
'''
async def hello_world():
    print("Hello")
    await asyncio.sleep(1)
    print("World")

# print(hello_world()) #  coroutine 创建了协程对象
asyncio.run(hello_world()) # 运行协程对象

