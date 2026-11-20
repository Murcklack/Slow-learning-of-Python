with open("movies.txt", "r", encoding="utf-8") as f:
    first = f.readline().strip().split(";")
    five = []

    minimum = 2030
    maximum = 0
    for count, line in enumerate(f, start=1):
        normal_line = line.strip().split(";")
        if count <= 5:
            five += [normal_line]
        maximum = max(maximum, int(normal_line[1]))
        minimum = min(minimum, int(normal_line[1]))

    print(f"Число строк данных(без заголовка): {count}")
    print("названия столбцов")
    print(" ".join(first) + "\n")
    print("первые 5 записей в читаемом виде")
    for x in five:
        clean = " | ".join(x)
        print(clean)
    print(
        f"минимальный = {minimum} и максимальный = {maximum} год выпуска среди записей"
    )
