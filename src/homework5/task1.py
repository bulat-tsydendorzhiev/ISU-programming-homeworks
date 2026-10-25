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

            if clean_line == "roles:" or clean_line == "textLines:":
                current_section = clean_line[:-1]
                continue

            if current_section == "roles":
                roles.append(clean_line)
            else:
                text_lines.append(clean_line)

    return (roles, text_lines)


def group_roles_text(roles: list[str], text_lines: list[str]) -> dict[str, list[tuple[int, str]]]:
    """Группирует реплики по ролям, нумеруя реплики по их номеру строки."""
    roles_text: dict[str, list[tuple[int, list[str]]]] = {role: [] for role in roles}
    current_role = None

    for i, text_line in enumerate(text_lines):
        separator = text_line.find(":")
        role = text_line[:separator] if separator > 0 else None

        if role in roles_text:
            current_role = role
            text = text_line[separator + 1:]
            roles_text[role].append((i + 1, [text.strip()] if text else []))
            continue

        if current_role is not None and roles_text[current_role]:
            roles_text[current_role][-1][1].append(text_line)

    return {
        role: [(line_number, "\n".join(parts)) for line_number, parts in replicas if parts]
        for role, replicas in roles_text.items()
    }


def main() -> None:
    if sys.argv[1] in ("-h", "--help"):
        message = "Чтобы запустить программу введите python -m \"путь к этому файлу модуля\" <путь к текстовому файлу>."
        print(message)
        return

    if len(sys.argv) != 2:
        print("Некорректное число аргументов. Введите флаг -h или --help для больших деталей.")
        return

    path = sys.argv[1]

    if not os.path.isfile(path):
        print("Такого файла не существует. Введите флаг -h или --help для больших деталей.")
        return

    if not path.endswith(".txt"):
        print("Программа работает только с текстовыми файлами. Введите флаг -h или --help для больших деталей.")
        return

    roles, text_lines = get_roles_and_text_lines(path)
    roles_text = group_roles_text(roles, text_lines)

    for role in roles_text:
        print(f"{role}:")
        for line_number, text in roles_text[role]:
            print(f"{line_number}) {text}")
        print()


if __name__ == "__main__":
    main()