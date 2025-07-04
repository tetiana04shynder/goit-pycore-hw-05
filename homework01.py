def total_salary(path):
    try:
        total = 0
        count = 0
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                print(f"Обробити рядок: {line.strip()}")
                parts = line.strip().split(',')
                if len(parts) != 2:
                    continue
                try:
                    salary = float(parts[1])
                except ValueError:
                    continue
                total += salary
                count += 1

        if count == 0:
            return (0, 0)
        average = total / count
        return (total, average)

    except FileNotFoundError:
        print(f"Файл за шляхом '{path}' не знайдено.")
        return (0, 0)

if __name__ == "__main__":
    total, average = total_salary("/Users/taniashynder/Desktop/salary_file.txt")
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")

