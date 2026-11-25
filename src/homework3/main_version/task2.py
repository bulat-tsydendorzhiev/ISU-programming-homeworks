

def find_first_occurence(number: str) -> int:
    """Находит первое вхождение числа в строке вида '0123456789101112...'"""

    numbers_string = "".join(str(i) for i in range(1, int(number) + 1))

    return numbers_string.find(number) + 1

def main() -> None:
    n = input("Введите натуральное число до 10^4: ")
    if not str.isdigit(n):
        print("Введенная строка не является числом")
        return

    if not(0 < int(n) <= 10000):
        print("Введеное число должно быть натуральным числом в диапазоне от 1 до 10^4")
        return
    
    print(f"Первое вхождение числа в натуральном ряде: {find_first_occurence(n)}")

if __name__ == "__main__":
    main()