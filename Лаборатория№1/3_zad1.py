def read_file(filename, mode="all"):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            if mode == "all":
                # Чтение всего файла сразу
                content = file.read()
                print("Содержимое файла полностью:\n")
                print(content)
            elif mode == "lines":
                # Построчное чтение
                print("Чтение файла построчно:\n")
                for line in file:
                    print(line.strip())
            else:
                print("Неверно указан режим. Используйте 'all' или 'lines'.")
    except FileNotFoundError:
        print(f"Ошибка: файл '{filename}' не найден.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")


# Пример вызовов:
read_file("example.txt", "all")     # Чтение всего файла
print("\n---\n")
read_file("example.txt", "lines")   # Построчное чтение
