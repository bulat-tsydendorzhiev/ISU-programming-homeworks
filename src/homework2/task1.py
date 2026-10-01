# Смещения относительно занятой ячейки: (строка, столбец).
DIRECTIONS = ((-1, 0), (1, 0), (0, -1), (0, 1))


def count_placement_positions(field: list[str]) -> int:
    """Считает число способов поставить оставшийся однопалубный корабль."""
    n, m = len(field), len(field[0])
    blocked = [[False] * m for _ in range(n)]

    for row, line in enumerate(field):
        for col, cell in enumerate(line):
            if cell != "*":
                continue
            blocked[row][col] = True
            for d_row, d_col in DIRECTIONS:
                r, c = row + d_row, col + d_col
                if 0 <= r < n and 0 <= c < m:
                    blocked[r][c] = True

    return sum(not blocked[row][col] for row in range(n) for col in range(m))

if __name__ == "__main__":
    n, _ = map(int, input().split())
    field = [input().strip() for _ in range(n)]
    print(count_placement_positions(field))