#当你对一个对象使用 | 运算符时，Python 会尝试调用该对象的 __or__ 方法
# a | b 实际上调用了 a.__or__(b)

class MySet:
    def __init__(self, elements):
        self.elements = set(elements)

    def __or__(self, other):
        """实现集合的并集操作"""
        return MySet(self.elements.union(other.elements))

    def __repr__(self):
        return f"MySet({self.elements})"


# 创建两个自定义集合
set1 = MySet([1, 2, 3])
set2 = MySet([3, 4, 5])

set3= MySet([6, 7, 8])

# 使用 | 运算符计算并集
# result = set1 | set2
# print(result)  # 输出: MySet({1, 2, 3, 4, 5})

result=set1 | set2 | set3
# set1 | set2 返回对象还是MySet
print(result)  # 输出: MySet({1, 2, 3, 4, 5, 6, 7, 8})
