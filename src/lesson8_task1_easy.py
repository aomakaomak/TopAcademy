
# Задание 1   Если у нас только пробелы

while True:
    my_string = input("Введите любое предложение: \n")
    if my_string:
        lower_string = my_string.lower().replace(' ', '')
        reverse_string = lower_string[::-1]
        print(lower_string)
        print(reverse_string)
        if reverse_string == lower_string:
            print("Строка является палиндромом")
        else:
            print("Строка НЕ является палиндромом")
        break
    else:
        question = input('Вы ничего не ввели. Хотите начать заново? Если да, введите любые символы, если нет - нажмите Enter: \n')
        if not question:
            break
