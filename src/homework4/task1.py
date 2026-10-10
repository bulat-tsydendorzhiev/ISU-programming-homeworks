

def main() -> None:
    while True:
        try:
            number_of_records = int(input("Введите количество записей в словаре: "))
            if number_of_records < 0:
                print("Число записей не может быть отрицательным.")
                continue
            break

        except ValueError:
            print("Числом записей может быть только натуральное число.")

    print(f"Введите {number_of_records} строк(и) в формате 'слово0 - слово_1, слово2, ..., слово_m':")

    records = {}

    while len(records) < number_of_records:
        row = input()

        if not row:
            print("Строка не может быть пустой.")
            continue

        english_and_latins = row.split('-')

        if not english_and_latins[0]:
            print("Английское слово не может быть пустой строкой.")
            continue

        latin_words = [word.strip() for word in english_and_latins[1].split(',')]

        if len(latin_words) == 0:
            print("Строка не содержит латинских слов.")
            continue

        records[english_and_latins[0]] = latin_words


if __name__ == "__main__":
    main()