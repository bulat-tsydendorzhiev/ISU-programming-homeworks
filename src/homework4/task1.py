

def invert_dictionary(eng_to_lat: dict[str, list[str]]) -> dict[str, list[str]]:
    """Преобразует англо-латинский словарь в латино-английский."""
    inverted_dictionary = {}

    for english_word in eng_to_lat:
        for latin_word in eng_to_lat[english_word]:
            inverted_dictionary.setdefault(latin_word, []).append(english_word)

    return dict(sorted(inverted_dictionary.items()))
    

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
            print("Английское слово не может быть пустой строкой. Запись не добавлена.")
            continue

        latin_words = [word.strip() for word in english_and_latins[1].split(',')]

        if len(latin_words) == 0:
            print("Строка не содержит латинских слов, поэтому не была добавленая в словарь.")
            continue

        records[english_and_latins[0]] = latin_words

    print("---------------")
    inverted_dictionary = invert_dictionary(records)

    print(len(inverted_dictionary))
    for latin_word in inverted_dictionary:
        print(f"{latin_word} - {",".join(inverted_dictionary[latin_word])}")


if __name__ == "__main__":
    main()