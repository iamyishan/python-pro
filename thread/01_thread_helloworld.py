# import threading
#
# class MyThread(threading.Thread):
#     def run(self):
#         print("线程开始执行")
#         # 在这里编写线程要执行的代码
#         print("线程执行结束")
#
# # 创建线程实例
# thread = MyThread()
# # 启动线程
# thread.start()
# # 等待线程执行完毕
# thread.join()
# print("主线程结束")

import threading
import time

def worker():
    print("子线程开始执行")
    time.sleep(2)
    print("子线程执行完毕")

# 创建并启动子线程
t = threading.Thread(target=worker)
t.start()

print("主线程等待子线程完成...")
t.join()  # 主线程会在这里等待子线程执行完毕
print("所有工作完成，主线程退出")