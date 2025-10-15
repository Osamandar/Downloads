a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))

if a == b:
    print("Числа равны:", a)
else:
    if a > b:
        larger = a
    else:
        larger = b
    print("Большее число:", larger)
if a > 0 and b > 0:
    print("Оба числа положительные.")
elif a < 0 and b < 0:
    print("Оба числа отрицательные.")
else:
    print("Одно из чисел положительное, другое отрицательное.")
