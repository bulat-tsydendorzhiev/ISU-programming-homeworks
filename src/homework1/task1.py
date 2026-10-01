def get_non_unique_numbers(numbers: list[int]) -> list[int]:
    """
    Возвращает список чисел, которые встречаются в списке более одного раза.
    """

    seen = set()
    duplicates = set()

    for num in numbers:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)

    return list(duplicates)

if __name__ == "__main__":
    numbers = list(map(int, input("Введите список чисел через пробел: ").split()))
    print(*get_non_unique_numbers(numbers))
