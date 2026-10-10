

KEY_PHRASE = "the quick brown fox jumps over the lazy dog"


def is_decoded_key_phrase(row: str):
    """Проверяет является ли строка закодированной ключевой фразой"""
    return (len(row) == len(KEY_PHRASE) 
            and len(set(row)) == 27 
            and all((row[i] == ' ') == (KEY_PHRASE[i] == ' ') for i in range(len(KEY_PHRASE))))


def decode_letter(letter: list[str]) -> list[str]:
    """Расшифровывает письмо по зашифрованному ключевому слову."""
    table: dict[str, str] = None

    for row in letter:
        if is_decoded_key_phrase(row):
            table = str.maketrans(dict(zip(row, KEY_PHRASE)))
            break

    if table is None:
        return ["No solution"]

    return [row.translate(table) for row in letter]

    

if __name__ == "__main__":
    n = int(input())
    letter = [input().strip() for _ in range(n)]
    
    decoded = decode_letter(letter)

    for row in decoded:
        print(row)
