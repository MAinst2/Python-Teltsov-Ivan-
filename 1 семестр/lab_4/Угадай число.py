import random
import time
from datetime import datetime


def get_guess():
    while True:
        try:
            return int(input("Твой вариант: "))
        except ValueError:
            print("Введи целое число!")


def save_stats(result: str, attempts: int, total_time: float, move_times: list):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("game_stats.txt", "a", encoding="utf-8") as f:
        f.write(f"[{now}] {result}. Попытки: {attempts}, Общее время: {round(total_time, 2)} сек.\n")
        for idx, t in enumerate(move_times, 1):
            f.write(f"\tХод {idx}: {round(t, 2)} сек\n")
        f.write("\n")


def play_game():
    number = random.randint(1, 100)
    attempts = 0
    total_start = time.time()
    move_times = []

    print("Я загадал число от 1 до 100. Попробуй угадать!")

    while True:
        move_start = time.time()
        guess = get_guess()
        move_end = time.time()

        move_duration = move_end - move_start
        move_times.append(move_duration)
        print(f"⏱️ Время на ответ: {round(move_duration, 2)} сек.\n")

        attempts += 1

        if guess < number:
            print("Слишком маленькое число.\n")
        elif guess > number:
            print("Слишком большое число.\n")
        else:
            total_time = time.time() - total_start
            print(f"✅ Угадал! Это число {number}.")
            print(f"Попыток: {attempts}")
            print(f"Общее время: {round(total_time, 2)} сек.")
            save_stats("Угадал", attempts, total_time, move_times)
            break


if __name__ == "__main__":
    play_game()
