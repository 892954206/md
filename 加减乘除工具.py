def simple_calculator():
    print("=== 简易计算器 ===")
    print("支持运算：加法(+), 减法(-), 乘法(*), 除法(/)")
    
    try:
        # 用户输入数字和运算符
        num1 = float(input("请输入第一个数字: "))
        operator = input("请输入运算符 (+, -, *, /): ")
        num2 = float(input("请输入第二个数字: "))

        # 根据运算符计算结果
        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            if num2 == 0:
                raise ValueError("除数不能为零！")
            result = num1 / num2
        else:
            raise ValueError("无效的运算符！")

        # 输出结果
        print(f"结果: {num1} {operator} {num2} = {result:.2f}")

    except ValueError as e:
        print(f"输入错误: {e}")
    except Exception as e:
        print(f"发生未知错误: {e}")

# 运行计算器
if __name__ == "__main__":
    while True:
        simple_calculator()
        choice = input("\n是否继续？(y/n): ").lower()
        if choice != 'y':
            print("感谢使用！")
            break
