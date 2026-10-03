

def get_passenger_count(time_intervals: list[(int, int)], target_time: int) -> int:
    """
    Получает количество пассажиров, находящихся в метро на момент времени target_time.
    """
    passengers_count = 0

    for _, (entry_time, exit_time) in enumerate(time_intervals):
        if entry_time <= target_time <= exit_time:
            passengers_count += 1

    return passengers_count

if __name__ == "__main__":
    passenger_numbers = int(input("Введите число пассажиров в метро: "))

    time_intervals = []

    for _ in range(passenger_numbers):
        entry_time, exit_time = map(int, input().split())
        time_intervals.append((entry_time, exit_time))

    target_time = int(input("Введите время, для которого хотите узнать количество пассажиров в метро: "))

    print(f"Число пассажиров в метро на переданный момент времени: {get_passenger_count(time_intervals, target_time)}")
