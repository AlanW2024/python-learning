# 猜数字游戏改进版
import random

print("猜数字游戏开始！")
print("(输入'q'随时退出游戏)")
target = random.randint(1, 100)
guess_count = 0

while True:
    # 获取用户输入并处理可能的错误
    try:
        user_input = input("猜一个1到100之间的数字：")
        
        # 检查是否要退出
        if user_input.lower() == 'q':
            print("游戏结束！")
            break
            
        # 转换输入为数字
        guess = int(user_input)
        
        # 检查数字范围
        if guess < 1 or guess > 100:
            print("请输入1到100之间的数字！")
            continue
            
        guess_count += 1
        
        # 判断结果
        if guess < target:
            print("太小了！")
        elif guess > target:
            print("太大了！")
        else:
            print(f"恭喜你猜对了！共猜了{guess_count}次")
            break
            
    except ValueError:
        print("请输入有效的数字！")
        continue 