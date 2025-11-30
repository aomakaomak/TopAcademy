import random

secret = random.randint(1, 10)
print(secret)

while True:
    choice = int(input("Введите число"))

    if (0 < (secret - choice) <= 2) or (0 < (choice - secret) <= 2):
        print("Горячо")
    elif (2 < (secret - choice) <= 4) or (2 < (choice - secret) <= 4):
        print("Тепло")
    elif ((secret - choice) > 4) or ((choice - secret) > 4):
        print("Холодно")
    else:
        print(f"Вы угадали. Это число {secret}")
        break
