from calculator import calculate   # Взимаме функцията от calculator.py

def main():
    """Главна функция на калкулатора."""
    while True:
        num = float(input("Въведете първото си число: "))
        sign = input("Въведете операцията (+, -, *, /, ^, %, exit): ")

        if sign == "exit":
            print("Излизане от калкулатора...")
            break

        num_two = float(input("Въведете второто си число: "))

        result = calculate(num, sign, num_two)
        print(f"Резултат: {result}\n")

# Стартира програмата САМО ако това е главният файл
if __name__ == "__main__":
    main()