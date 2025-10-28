while True:
    num = float(input("Въведете първото си число: "))
    sign = input("Въведете операцията която ще използвате (+, -, *, /, ^, %, exit): ")

    if sign == "exit":
        print("Излизане от калкулатора . . .")
        break

    num_two = float(input("Въведете второто си число: "))

    if sign == "+":
        result = num + num_two
    elif sign == "-":
        result = num - num_two
    elif sign == "*":
        result = num * num_two
    elif sign == "/":
        if num_two == 0:
            print("Деление на нула, не може!")
            continue
        result = num / num_two
    elif sign == "^":
        result = num ** num_two
    elif sign == "%":
        result = num % num_two
    else:
        print("Няма такава операция!")
        continue

    print(f"Резултат: {result}\n")
