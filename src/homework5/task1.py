import sys
import os


def get_roles_and_text_lines(path: str) -> tuple[list[str], list[str]]:
    """Возвращает списки ролей и реплик из текстового файла."""
    roles = []
    text_lines = []
    current_section = None

    with open(path, "r", encoding="utf-8") as file:
        for line in file:
            clean_line = line.strip()

            if clean_line == "roles:":
                current_section = "roles"
                continue
            elif clean_line == "textLines:":
                current_section = "lines"
                continue

            if current_section == "roles":
                roles.append(clean_line)
            elif current_section == "lines":
                text_lines.append(clean_line)

    return (roles, text_lines)


def main() -> None:
    if len(sys.argv) != 2:
        print("Некорректное число аргументов. Введите флаг -h или --help для больших деталей.")
        return

    if sys.argv[0] in ("-h", "--help"):
        # TODO написать сообщение для пользователя.
        print()
        return

    path = sys.argv[1]

    if not os.path.isfile(path):
        print("Такого файла не существует.")
        return

    roles, text_lines = get_roles_and_text_lines(path)


if __name__ == "__main__":
    main()