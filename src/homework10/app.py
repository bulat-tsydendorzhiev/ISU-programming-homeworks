import json
import argparse
import os
from datetime import datetime


def create_users_json(users: list) -> str:
    """Принимает список пользователей и возвращает валидную JSON-строку."""
    return json.dumps(users, ensure_ascii=False, indent=4)


def parse_users_json(json_string: str) -> list:
    """Принимает JSON-строку, валидирует её и возвращает список пользователей.
    
    Бросает ValueError, если JSON некорректен.
    """
    try:
        data = json.loads(json_string)
        if not isinstance(data, list):
            raise ValueError("Корневой элемент JSON должен быть списком.")
        return data
    
    except json.JSONDecodeError as e:
        raise ValueError(f"Некорректный формат JSON: {e}")


def collect_users_from_console():
    """Интерактивный сбор данных из консоли (UI-слой)."""
    print("--- Режим генерации данных о пользователях ---")
    print("--- Введите пустую строку при вводе логина пользователя для выхода из программы ---")
    users = []

    while True:
        try:
            user_login = input("Введите логин пользователя: ")
            if not user_login:
                break

            user_last_login = input("Введите время последнего входа (YYYY-MM-DD HH:mm:ss): ")
            datetime.strptime(user_last_login, "%Y-%m-%d %H:%M:%S")

            if len(user_last_login) != 19:
                raise ValueError("Лишние символы в строке даты")

            user_session_duration = int(input("Введите длительность сессии (в минутах): "))
            if user_session_duration < 0:
                raise ValueError("Некорректное время сессии.")

            user_data = {
                "login": user_login,
                "last_login": user_last_login,
                "session_duration_minutes": user_session_duration
            }
            users.append(user_data)

        except ValueError as e:
            print(e)

    return users


def format_users_for_display(users: list) -> str:
    """Превращает список пользователей в красивую строку для вывода на экран."""
    if not users:
        return "Список пользователей пуст."

    LINE_LENGTH = 40
    lines = [f"\nНайдено пользователей: {len(users)}", "-" * LINE_LENGTH]
    for idx, user in enumerate(users, 1):
        lines.append(f"Пользователь №{idx}:")
        lines.append(f"Логин: {user.get('login', 'Не указано')}")
        lines.append(f"Последняя сессия: {user.get('last_login', 'Не указано')}")
        lines.append(f"Длительность сессии: {user.get('session_duration_minutes', 'Не указано')}")
        lines.append("-" * LINE_LENGTH)
    
    return "\n".join(lines)


def handle_generate(filename: str):
    """Контроллер команды generate."""
    users = collect_users_from_console()
    if not users:
        print("Данные не были введены. Файл не создан.")
        return

    json_data = create_users_json(users)
    
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(json_data)
        print(f"Файл '{filename}' успешно создан.")
    except IOError as e:
        print(f"Ошибка при записи файла: {e}")


def handle_parse(filename: str):
    """Контроллер команды parse."""
    if not os.path.exists(filename):
        print(f"Ошибка: Файл '{filename}' не найден.")
        return

    if not filename.endswith(".json"):
        print(f"Ошибка: файл должен заканчиваться на .json")
        return

    try:
        with open(filename, 'r', encoding='utf-8') as f:
            file_content = f.read()
        
        users = parse_users_json(file_content)
        print(format_users_for_display(users))
        
    except ValueError as e:
        print(f"Ошибка разбора: {e}")
    except IOError as e:
        print(f"Ошибка чтения файла: {e}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Программа для генерации и разбора JSON файлов с данными пользователей."
    )

    subparsers = parser.add_subparsers(dest="command", required=True, help="Доступные команды")
    
    gen_parser = subparsers.add_parser("generate", help="Создать JSON")
    gen_parser.add_argument(
        "-f", "--file", 
        default="users.json",
        help="Путь к файлу, куда будут сохраняться данные пользователей (по умолчанию users.json)")

    parse_parser = subparsers.add_parser("parse", help="Прочитать JSON")
    parse_parser.add_argument(""
        "-f", "--file", 
        default="users.json", 
        help="Путь к файлу, откуда будут читаться данные пользователей (по умолчанию users.json)")

    args = parser.parse_args()

    if args.command == "generate":
        handle_generate(args.file)
    elif args.command == "parse":
        handle_parse(args.file)
