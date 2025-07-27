#!/usr/bin/python3

import sys


def fibonacci(n):  # 生成器函数 - 斐波那契
    a, b, counter = 0, 1, 0
    while True:
        if (counter > n):
            return
        yield a
        a, b = b, a + b
        counter += 1


f = fibonacci(10)  # f 是一个迭代器，由生成器返回生成

# try:
# #     print(next(f), end=" ")
# # except StopIteration:
# #     sys.exit()
# # while True:

for item in f:
    print(item)


class Timer:
    def __enter__(self):
        import time
        self.start = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        import time
        self.end = time.time()
        print(f"耗时: {self.end - self.start:.2f}秒")
        return False


# 使用示例
with Timer() as t:
    # 执行一些耗时操作
    sum(range(1000000))