def greet() -> None:
    name = input("Введите ваше имя: ").strip()
    print(f"Привет, {name}!")
def square() -> None:
    while True:
        try:
            number = float(input("Введите число, чтобы узнать его квадрат: "))
            print(f"Квадрат числа {number} = {number ** 2}")
            break
        except ValueError:
            print("Ошибка: введите корректное число!")
def max_of_two() -> None:
    while True:
        try:
            a = float(input("Введите первое число: "))
            b = float(input("Введите второе число: "))
            larger = a if a > b else b
            print(f"Большее число: {larger}")
            break
        except ValueError:
            print("Ошибка: введите корректные числа!")
if __name__ == "__main__":
    greet()
    print()
    square()
    print()
    max_of_two()