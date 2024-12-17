import random

rand = random.randint(0, 10)
attempts = 0  

while True:
    user_input = input("Введите число: ")

    
    try:
        user_number = int(user_input)
    except ValueError:
        print("Пожалуйста, введите корректное целое число.")
        continue  

    attempts += 1  

    if user_number == rand:
        print(f"Вы ввели правильное число! Количество попыток: {attempts}")
        break
    elif user_number > rand:
        print("Число меньше")  
    else:
        print("Число больше")  

