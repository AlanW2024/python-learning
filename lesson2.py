# 第二课：控制流程

# 1. if-elif-else 条件语句
age = int(input("请输入你的年龄："))
print("条件语句示例：")

if age >= 18:
    print("你是成年人")
else:
    print("你是未成年人")

# 多重条件判断
score = 85
print("成绩评级：")

if score >= 90:
    print("优秀")
elif score >= 80:
    print("良好")
elif score >= 60:
    print("及格")
else:
    print("不及格")

# 2. while 循环
print("while循环示例：")
count = 0
while count < 5:
    print(f"当前计数：{count}")
    count += 1

# 3. for 循环
print("for循环示例：")
fruits = ["苹果", "香蕉", "橙子"]
for fruit in fruits:
    print(f"水果：{fruit}")

# 使用range()
print("使用range()的for循环：")
for i in range(5):    # 0到4
    print(f"数字：{i}")

# 4. break和continue
print("break示例：")
for i in range(5):
    if i == 3:
        break
    print(f"数字：{i}")

print("continue示例：")
for i in range(5):
    if i == 2:
        continue
    print(f"数字：{i}")

# 5. 实践：猜数字游戏
import random

print("猜数字游戏开始！")
target = random.randint(1, 100)
guess_count = 0

while True:
    guess = int(input("猜一个1到100之间的数字："))
    guess_count += 1
    
    if guess < target:
        print("太小了！")
    elif guess > target:
        print("太大了！")
    else:
        print(f"恭喜你猜对了！共猜了{guess_count}次")
        break 