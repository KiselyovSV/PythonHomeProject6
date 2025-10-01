def main():
    print("Diet start")

    diet("гречка", "курица", "шашлык", "бургер", "печенье", "фрукты", "конфеты")

def diet(*eats: str):
    healthy_f_count = 0
    food = {
        'жирное': ['бургер', 'пицца', 'шашлык'],
        'сладкое': ['торт', 'мороженое', 'конфеты'],
        'мучное': ['булочки', 'печенье', 'хлеб'],
        'диетическое': ['овощи', 'фрукты', 'гречка', 'курица']
    }
    for eat in eats:
        for key in food:
            for i in food[key]:
                if i == eat and key == "диетическое":
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