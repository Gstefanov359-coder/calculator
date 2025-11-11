def calculate(num, sign, num_two):
    """Функцията прави математическата операция."""
    if sign == "+":
        return num + num_two
    elif sign == "-":
        return num - num_two
    elif sign == "*":
        return num * num_two
    elif sign == "/":
        if num_two == 0:
            return "Грешка: Деление на нула!"
        return num / num_two
    elif sign == "^":
        return num ** num_two
    elif sign == "%":
        return num % num_two
    else:
        return "Грешка: Няма такава операция!"