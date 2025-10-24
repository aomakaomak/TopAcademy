
# ТАКЖЕ в файле https://github.com/aomakaomak/TopAcademy/blob/main/src/task1_var2.py
# СДЕЛАЛ ФУНКЦИЮ И ОБРАБОТАЛ ИСКЛЮЧЕНИЯ


salary = input("Введите свою зарплату: ")
mortgage = input("Введите процент по ипотеке: ")
life = input("Введите процент на жизнь: ")

if not salary.isdigit() or not mortgage.isdigit() or not life.isdigit():
    print("Не выпендривайтесь. Вводите числа!")
elif int(mortgage) > 100:
    print("Да вы совсем безбашенный")
elif (int(mortgage) + int(life)) > 100:
    print("А раньше головой нужно было думать, а не чем обычно")
else:
    print(f"На ипотеку было потрачено: {int(int(salary)*int(mortgage)/100*12)} рублей")
    print(
        f"Было накоплено: {int((int(salary)-int(salary)*int(mortgage)/100-int(salary)*int(life)/100)*12)} рублей"
    )
