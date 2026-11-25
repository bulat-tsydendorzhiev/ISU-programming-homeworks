import json
import sys

def dump_to_file(path: str, data):
    with open(path, 'w', encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def get_user_input():
    data = []

    while True:
        try:
            user_login = input("Введите логин пользователя: ")
            user_last_login = input("Введите время последнего входа (YYYY-MM-DD HH:mm:ss): ")
            user_session_duration = input("Введите длительность сессии (в минутах): ")

            user_data = {
                "login": user_login,
                "last_login": user_last_login,
                "session_duration_minutes": user_session_duration
            }
            data.append(user_data)

        except ValueError:
            print("Неверно введено значение ")

def read_json_file(path: str):
    with open(path, 'r', encoding="utf-8") as f:
        data = json.load(f)

    return data

if __name__ == "__main__":
    pass