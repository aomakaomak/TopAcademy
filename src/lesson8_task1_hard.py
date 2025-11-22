


# Задание 1 -- убираем любые символы из предложения, не только пробелы. Можно вводить любые символы ( скобки, слэши и т.д.) - и они не учтутся

import string

while True:
    symbols_for_delete = string.punctuation + ' '

    string_comp = input("Введите любое предложение: \n")

    if string_comp:
        string_with_all_symbols = string_comp.lower()

        symbols = []
        for symbol in string_with_all_symbols:
            if symbol not in symbols_for_delete:
                symbols.append(symbol)
        user_string = ''.join(symbols)
        reverse_string = user_string[::-1]
        if user_string == reverse_string:
            print("Строка является палиндромом")
        else:
            print("Строка НЕ является палиндромом")
        break
    else:
        question = input('Вы ничего не ввели. Хотите начать заново? Если да, введите любые символы, если нет - нажмите Enter: \n')
        if not question:
            break