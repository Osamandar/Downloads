def describe_person():
    name = input("Введите имя: ").strip().capitalize()
    while True:
        a = input("Введите возраст").strip()
        if not a:
            a = 30
            break
        if a.isdigit() and 1 <= int(a) <= 99:
            a = int(a)
            break
        print("Некорректный возраст!")
    print(f"\nИмя: {name}\nВозраст: {a} лет\n")
describe_person()
