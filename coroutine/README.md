# Python协程教程

本项目提供了一系列Python协程（coroutine）的示例代码，从基础概念到高级用法，帮助开发者逐步掌握异步编程的核心技能。

## 目录结构

| 文件名称 | 说明 |
|----------|------|
| `01_asyncio_helloword.py` | 协程基础示例，演示最简单的异步函数定义与运行 |
| `02_asyncio_basic.py` | 基础任务管理，使用`asyncio.ensure_future()`创建任务 |
| `03_asyncio_task.py` | 任务回调机制，展示如何使用`add_done_callback()`处理任务结果 |
| `04_asyncio_new_grammar.py` | 新版语法示例，使用`asyncio.create_task()`和`asyncio.gather()`管理任务 |

## 环境要求
- Python 3.7+（推荐3.9以上版本以获得最佳异步支持）

## 运行方法

### 单个文件运行
```bash
# 运行基础示例
python 01_asyncio_helloword.py

# 运行任务管理示例
python 03_asyncio_task.py

# 运行新版语法示例
python 04_asyncio_new_grammar.py
```

## 核心概念讲解

### 协程对象
使用`async def`定义的函数会创建协程对象，需通过事件循环运行：
```python
async def hello_world():
    print("Hello")
    await asyncio.sleep(1)
    print("World")

asyncio.run(hello_world())  # Python 3.7+新语法
```

### 任务管理
- **旧版语法**：`asyncio.ensure_future()`创建任务
- **新版语法**：`asyncio.create_task()`创建任务（推荐）
- 任务结果获取：`task.result()`或通过`add_done_callback()`回调函数
- 批量任务运行：`asyncio.gather(*tasks)`

## 学习资源
- [Python官方asyncio文档](https://docs.python.org/3/library/asyncio.html)
- [协程与任务](https://docs.python.org/3/library/asyncio-task.html)
- [异步IO编程指南](https://docs.python.org/3/library/asyncio-dev.html)

## 许可证
本项目基于Apache License 2.0开源协议，详情参见项目根目录下的LICENSE文件。