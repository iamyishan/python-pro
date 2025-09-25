from concurrent.futures import ThreadPoolExecutor
import time
import random

def task(task_id):
    print(f"任务 {task_id} 开始执行\n")
    # 模拟任务执行时间
    time.sleep(random.uniform(0.5, 2.0))
    print(f"任务 {task_id} 执行完成")
    return f"任务 {task_id} 的结果"


def main():
    # 创建线程池，指定最大线程数为3
    with ThreadPoolExecutor(max_workers=3) as executor:
        # 提交5个任务到线程池
        tasks = [executor.submit(task, i) for i in range(1, 6)]

        # 获取所有任务的结果
        for future in tasks:
            result = future.result()  # 阻塞直到任务完成并获取结果
            print(f"收到结果: {result}")


if __name__ == "__main__":
    main()