

def count_subprefix_matches(dictionary: list[str], samples: list[str]) -> dict[str, int]:
    """Считает для каждой строки-образца совпадения по критерию супрефикса."""
    matches = {}

    for word in dictionary:
        for sample in samples:
            if sample not in matches:
                matches[sample] = 0

            if word.find(sample) == 0 and word.rfind(sample) == len(word) - len(sample):
                matches[sample] += 1

    return matches


if __name__ == "__main__":
    n = int(input("Введите число n: "))
    print("Введите n строк слов, являющихся словарем:")
    dictionary = [input() for _ in range(n)]

    m = int(input("Введите число m: "))
    print("Введите m строк слов, являющихся строками-образцами:")
    samples = [input() for _ in range(m)]

    subprefix_matches = count_subprefix_matches(dictionary, samples)
    for sample in samples:
        print(subprefix_matches[sample])
