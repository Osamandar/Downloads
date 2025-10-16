def read_file(filename: str, mode: str = "all") -> None:
    """
    Читает файл и выводит его содержимое.

    :param filename: имя файла
    :param mode: режим чтения ('all' — весь файл, 'lines' — построчно)
    """
    try:
        with open(filename, "r", encoding="utf-8") as f:
            if mode == "all":
                print(f.read())
            elif mode == "lines":
                for line in f:
                    print(line, end="")
            else:
                print("Ошибка: неизвестный режим чтения")
    except FileNotFoundError:
        print(f"Файл {filename} не найден!")
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")


# --- Пример использования ---
if __name__ == "__main__":
    filename = "example.txt"

    print("=== Чтение всего файла ===\n")
    read_file(filename, mode="all")

    print("\n=== Чтение построчно ===\n")
    read_file(filename, mode="lines")
