def main():
    print("Diet start")

    diet("гречка", "курица", "шашлык", "бургер", "печенье", "фрукты", "конфеты")

def diet(*eats: str) -> None:
    """
    Функция сравнивает введённые параметры с имеющимися и ведёт подсчёт полезных продуктов, если полезных больше,
    то выводит строку "На здоровье", если меньше, то - "Не ешь это"
    :param eats: str
    :return: None
    """
    healthy_f_count = 0
    food = {
        'жирное': ['бургер', 'пицца', 'шашлык'],
        'сладкое': ['торт', 'мороженое', 'конфеты'],
        'мучное': ['булочки', 'печенье', 'хлеб'],
        'диетическое': ['овощи', 'фрукты', 'гречка', 'курица']
    }
    for eat in eats:
         for i in food['диетическое']:
                if i == eat:
                    healthy_f_count += 1
    if healthy_f_count >= len(eats) / 2:
        print(f"Полезной еды: {healthy_f_count}\n"
              f"Вредной: {len(eats) - healthy_f_count}\n"
              f"На здоровье!")
    else:
        print(f"Полезной еды: {healthy_f_count}\n"
              f"Вредной: {len(eats) - healthy_f_count}\n"
              "Не ешь это!")


main()