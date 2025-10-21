num = int(input("Enter your first number "))
sign = input("Enter the sign (+, -, *, /): ")
num_two = int(input("Enter your second number "))
if sign == "+":
    print(num + num_two)
elif sign == "-":
    print(num - num_two)
elif sign == "*":
    print (num * num_two)
elif sign == "/":
    print(num / num_two)
else:
    print("I cant do it")