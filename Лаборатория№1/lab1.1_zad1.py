while True:
    try:
        num = int(input("Введите число: "))

        if num < 0:
            print("Число отрицательное. Пожалуйста, введите положительное число.")
            continue 

        if num > 0:
            print("Число положительное")
        else:
            print("Число равно нулю")

        if num % 2 == 0:
            print("Число четное")
        else:
            print("Число нечетное")

        if num > 0:
            print("Числа от 1 до", num, ":")
            for i in range(1, num + 1):
                print(i)

        break  

    except ValueError:
        print("Ошибка! Нужно вводить только целое число.")
