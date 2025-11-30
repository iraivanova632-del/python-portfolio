import random

number = random.randint(1, 100)
print("Я загадал число от 1 до 100!")

while True:
    guess = int(input("Ваш вариант: "))
    if guess < number:
        print("Больше!")
    elif guess > number:
        print("Меньше!")
    else:
        print("Угадали!")
        break