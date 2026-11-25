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

            # Если в пользовательском файле была пустая строка для удобства.
            if not clean_line:
                continue

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
            text = text_line[separator + 1:].strip()
            roles_text[role].append((i + 1 if text else i + 2, [text] if text else []))
            continue

        if current_role is not None and roles_text[current_role]:
            roles_text[current_role][-1][1].append(text_line)

    return {
        role: [(line_number, "\n".join(parts)) for line_number, parts in replicas if parts]
        for role, replicas in roles_text.items()
    }


def get_default_output_path(input_path: str) -> str:
    """Возвращает путь выходного файла рядом с входным."""
    root, extension = os.path.splitext(input_path)
    return f"{root}.grouped{extension}"


def write_roles_text(path: str, roles_text: dict[str, list[tuple[int, str]]]) -> None:
    """Записывает сгруппированные реплики в файл, выравнивая продолжения."""
    groups = []

    for role, replicas in roles_text.items():
        group = [f"{role}:"]

        for line_number, text in replicas:
            prefix = f"{line_number}) "
            text_lines = text.split("\n")
            group.append(prefix + text_lines[0])
            group.extend(" " * len(prefix) + line for line in text_lines[1:])

        groups.append("\n".join(group))

    result = "\n\n".join(groups)

    with open(path, "w", encoding="utf-8", newline="\n") as file:
        file.write(result)
        if result:
            file.write("\n")


def main() -> None:
    if len(sys.argv) > 1 and sys.argv[1] in ("-h", "--help"):
        message = (
            "Чтобы запустить программу введите python -m \"путь к этому файлу модуля\" "
            "<путь к текстовому файлу> [путь к выходному файлу]."
        )
        print(message)
        return

    if len(sys.argv) not in (2, 3):
        print("Некорректное число аргументов. Введите флаг -h или --help для больших деталей.")
        return

    input_path = sys.argv[1]
    output_path = sys.argv[2] if len(sys.argv) == 3 else get_default_output_path(input_path)

    if not os.path.isfile(input_path):
        print("Такого файла не существует. Введите флаг -h или --help для больших деталей.")
        return

    if not input_path.endswith(".txt"):
        print("Программа работает только с текстовыми файлами. Введите флаг -h или --help для больших деталей.")
        return

    roles, text_lines = get_roles_and_text_lines(input_path)
    roles_text = group_roles_text(roles, text_lines)

    try:
        write_roles_text(output_path, roles_text)
    except OSError as error:
        print(f"Не удалось записать файл: {error}")
        return

    print(f"Результат записан в файл: {output_path}")


if __name__ == "__main__":
    main()