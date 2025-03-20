def get_cats_info(path):
    cats_list = []

    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                parts = line.strip().split(",")
                if len(parts) == 3:
                    cat_info = {"id": parts[0], "name": parts[1], "age": int(parts[2])}
                    cats_list.append(cat_info)
                else:
                    print(f"Увага! Неправильний формат даних '{line.strip()}'")
    except FileNotFoundError:
        print("Файл не знайдено. Перевірте вказаний шлях!")
    return cats_list

# Example of function use
cats_info = get_cats_info("task_2/cats_info.txt")
print(cats_info)