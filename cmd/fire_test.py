# calculator.py
import fire

def add(x, y):
    return x + y

def multiply(x, y):
    return x * y

# 案例2: 将类转换为CLI
class Greeter:
    def hello(self, name="World"):
        return f"Hello, {name}!"

    def goodbye(self, name):
        return f"Goodbye, {name}!"
if __name__ == '__main__':
    fire.Fire({
        'add': add,
        'multiply': multiply
    })
    # 运行程序
    # python fire_test.py add 10 20
    # python fire_test.py multiply 4 5

    # 案例2: 将类转换为CLI
    fire.Fire(Greeter)


