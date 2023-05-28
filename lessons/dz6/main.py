from lessons.dz6.tools import get_words, shuffle_words, show_stats, save_history


def main():
    name = input("Введите свое имя: ")
    points = 0

    for i in get_words():
        print(f"Угадайте слово: {shuffle_words(i)}")  # noqa: T201
        answer = input()
        if answer.strip() == i:
            points += 10
            print("Верно! Вы получаете 10 очков.")  # noqa: T201
        else:
            print(f"Неверно! Верный ответ – {i}.")  # noqa: T201

    save_history(name, points)
    show_stats()


if __name__ == "__main__":
    main()
