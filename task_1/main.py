def total_salary(path):
    try:
        total_salary = 0
        num_developers = 0

        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                parts = line.strip().split(",")
                if len(parts) == 2:
                    try:
                        salary = int(parts[1])
                        total_salary += salary
                        num_developers += 1
                    except ValueError:
                        print(
                            f"Увага! Неправильний формат заробітної плати '{line.strip()}'"
                        )
                else:
                    print(f"Увага! Неправильний формат даних '{line.strip()}'")

# average salary calculation
        if num_developers > 0:
            average_salary = total_salary / num_developers
            return total_salary, average_salary
        else:
            print("Відсутня інформація про заробітні плати співробітників у даному файлі.")
            return 0, 0
        
# the case when the file is 
    except FileNotFoundError:
        print("Файл не знайдено. Перевірте вказаний шлях!")
        return 0, 0

# Example of function use
total, average = total_salary("task_1/salary_file.txt")
print(
    f"Загальна сума заробітної плати: {int(total)}, Середня заробітна плата: {int(average)}"
)