

def calculate_perimeter(figure: list[tuple[int, int]]) -> int:
    """Calculate the perimeter of the figure based on its coordinates on a chessboard."""
    cells = set(figure)

    # Смещения относительно занятой ячейки: (строка, столбец).
    directions = ((-1, 0), (1, 0), (0, -1), (0, 1))

    perimeter = 4 * len(figure)

    for x, y in figure:
        for dx, dy in directions:
            if (x + dx, y + dy) in cells:
                perimeter -= 1

    return perimeter

if __name__ == "__main__":
    n = int(input())
    figure = [tuple(map(int, input().split())) for _ in range(n)]
    print(calculate_perimeter(figure))