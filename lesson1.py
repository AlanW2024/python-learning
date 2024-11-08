# 第一课：Python基础

# 1. Hello World
print("Hello, World!")

# 2. 变量和数据类型
# 数字
age = 25          # 整数
price = 19.99     # 浮点数

# 字符串
name = "小明"

# 布尔值
is_student = True

# 打印变量
print("变量演示：")
print(f"年龄：{age}")
print(f"价格：{price}")
print(f"姓名：{name}")
print(f"是否学生：{is_student}")

# 3. 基本运算
print("基本运算演示：")
a = 10
b = 3

print(f"a = {a}, b = {b}")
print(f"加法：{a} + {b} = {a + b}")
print(f"减法：{a} - {b} = {a - b}")
print(f"乘法：{a} * {b} = {a * b}")
print(f"除法：{a} / {b} = {a / b}")
print(f"取余：{a} % {b} = {a % b}")

# 4. 字符串操作
print("字符串操作演示：")
first_name = "张"
last_name = "三"
full_name = first_name + last_name
print(f"姓名拼接：{full_name}")

# 5. 类型转换
print("类型转换演示：")
number_str = "100"
number_int = int(number_str)
print(f"字符串 '{number_str}' 转换为整数：{number_int}")
print(f"整数 {number_int} 转换为字符串：{str(number_int)}")

# 6. 用户输入
print("用户输入演示：")
user_input = input("请输入你的名字：")
print(f"你好，{user_input}！")
