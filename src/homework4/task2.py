

def translate_operation(query_operation: str) -> str:
    """Переводит операцию с запроса в формат операции для файла"""
    match query_operation:
        case "read":
            return "R"
        case "write":
            return "W"
        case "execute":
            return "X"
        case _:
            return "Invalid data"


def process_access_queries(files: dict[str, list[str]], queries: list[tuple[str, str]]) -> list[str]:
    """Обрабатывает список запросов на доступ к файлам и возвращает статус для каждого."""
    return ["OK" if translate_operation(operation) in files[file_name] else "Access denied" for operation, file_name in queries] 


def get_number(input_message: str, negative_value_message: str, value_error_message: str) -> int:
    """Получает число от пользователя."""
    while True:
        try:
            n = int(input(input_message))
            if n < 0:
                print(negative_value_message)
                continue
            return n

        except ValueError:
            print(value_error_message)


def main() -> None:
    number_of_files = get_number("Введите количество файлов (n): ",
                                 "Количество файлов не может быть отрицательным числом.",
                                 "Количеством записей может быть только натуральное число.")

    print(r"Введите n строк в формате '<название файла> <операции (через пробел)>' (доступны: R, W, X; пример: write text.txt):")

    files = {}
    while len(files) < number_of_files:
        row = input()
        
        if not row:
            print("Строка не может быть пустой. Запись не добавлена.")
            continue

        file_and_permissions = row.split()

        if len(file_and_permissions) < 0 or len(file_and_permissions) > 4:
            print("Некорректное число аргументов. Запись не добавлена.")
            continue

        if not all(file_and_permissions[i] in "RWX" for i in range(1, len(file_and_permissions))):
            print("Введена некорректная операция с файлом. Запись не добавлена.")
            continue

        files[file_and_permissions[0]] = file_and_permissions[1:]

    number_of_queries = get_number("Введите количество запросов к файлам (m): ",
                                 "Количество запросов не может быть отрицательным числом.",
                                 "Количеством записей может быть только натуральное число.")

    print(r"Введите m запросов к файлам в формате '<операция> <название файла>' (доступны: read, write, execute; пример: write text.txt):")

    queries = []
    while len(queries) < number_of_queries:
        row = input()

        if not row:
            print("Строка не может быть пустой. Запись не добавлена.")
            continue

        action_and_file = row.split()

        if (len(action_and_file) != 2):
            print("Данные введены не по формату. Запись не добавлена.")
            continue

        if action_and_file[0] not in ("read", "write", "execute"):
            print("Введена некорректная операция. Запись не добавлена.")
            continue

        queries.append(tuple(action_and_file))

    print(files)
    print(queries)

    responses = process_access_queries(files, queries)
    for response in responses:
        print(response)


if __name__ == "__main__":
    main()