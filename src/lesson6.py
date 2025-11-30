# Понятно, зачем в задание был указан цикл while: чтобы если мы ввели неверные значения, то чтобы
# программа опять у нас спрашивала ввод.

while True:
    try:
        days_quantity = int(input("Введите количество дней: "))

        if days_quantity <= 0 or days_quantity > 7:
            raise ValueError("Количество дней должно быть от 1 до 7")

        hours_quantaty = 0
        for i in range(1, days_quantity + 1):
            hours_per_day = int(input(f"Введите количество часов в день {i}: "))
            if hours_per_day <= 0 or hours_per_day > 24:
                raise ValueError("Количество часов должно быть от 1 до 24")
            hours_quantaty += hours_per_day

        print(f"На этой неделе у вас было учебных часов: {hours_quantaty}.")
        break

    except ValueError as e:
        print(f"Ошибка: {e}. Попробуйте еще раз")
