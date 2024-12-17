import random

cards = {
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10,
    'Валет': 2,
    'Дама': 3,
    'Король': 4,
    'Туз': 11
}

deck = list(cards.keys())

random.shuffle(deck)

user_points = 0
pc_points = 0


print("Добро пожаловать в игру с картами!")

while True:
    choice = input("Хотите взять карту? (y/n): ").strip().lower()
    
    if choice == 'n':
        if pc_points > user_points:
            print(f"Вы набрали {user_points} а PC набрал {pc_points} очков. PC выиграл спасибо за игру!")
        elif pc_points == user_points:
            print(f"Вы набрали {user_points} а PC набрал {pc_points} очков. Вы набрали одинаковое число чоков, ничья")
        else:
            print(f"Вы набрали {user_points} а PC набрал {pc_points} очков. Поздравляю вы выиграли!")
        break
    elif choice == 'y':
        if not deck:
            print("В колоде больше нет карт!")
            break
        #ход пк
        card = deck.pop()
        card_value = cards[card]
        pc_points += card_value
        #ход человека
        card = deck.pop()
        card_value = cards[card]
        user_points += card_value
        
        print(f"Вы взяли карту: {card} (достоинство: {card_value})")
        print(f"Ваши очки: {user_points}")
        
        if user_points > 21:
            print("Вы превысили 21 очко! Вы проиграли.")
            break
        elif user_points == 21:
            print("Поздравляем! Вы набрали ровно 21 очко! Вы выиграли!")
            break
        elif pc_points > 21:
            print("Поздравляем! По скольку PC набрал больше чем 21 очко! Вы выиграли!")
            break
        elif pc_points == 21:
            print("Сожалею! PC набрал ровно 21 очко! Вы проиграли!")
            break
    else:
        print("Пожалуйста, введите 'y' или 'n'.")

print("До свидания!")