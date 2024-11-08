# 第三课：函数

# 1. 基本函数定义和调用
def say_hello():
    print("你好！")

# 调用函数
print("1. 基本函数调用：")
say_hello()

# 2. 带参数的函数
def greet(name):
    print(f"你好，{name}！")

print("\n2. 带参数的函数：")
greet("小明")

# 3. 带默认参数的函数
def greet_with_time(name, time="早上"):
    print(f"{time}好，{name}！")

print("\n3. 带默认参数的函数：")
greet_with_time("小红")  # 使用默认时间
greet_with_time("小华", "下午")  # 指定时间

# 4. 返回值
def add_numbers(a, b):
    return a + b

print("\n4. 返回值：")
result = add_numbers(5, 3)
print(f"5 + 3 = {result}")

# 5. 多个返回值
def calculate(a, b):
    add = a + b
    subtract = a - b
    multiply = a * b
    divide = a / b
    return add, subtract, multiply, divide

print("\n5. 多个返回值：")
add, sub, mul, div = calculate(10, 2)
print(f"10 和 2 的运算结果：")
print(f"加法：{add}")
print(f"减法：{sub}")
print(f"乘法：{mul}")
print(f"除法：{div}")

# 6. 函数作为参数
def apply_operation(func, x, y):
    return func(x, y)

def multiply(a, b):
    return a * b

print("\n6. 函数作为参数：")
result = apply_operation(multiply, 4, 5)
print(f"4 × 5 = {result}")

# 7. Lambda函数（匿名函数）
square = lambda x: x * x
print("\n7. Lambda函数：")
print(f"5的平方是：{square(5)}")

# 主程序
if __name__ == "__main__":
    print("函数示例程序运行完成！")