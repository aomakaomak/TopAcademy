def savings(salary: str, mortgage: str, life: str) -> str:
    """Рассчитываем, сколько денег удалось накопить за год"""
    if not salary.isdigit() or not mortgage.isdigit() or not life.isdigit():
        raise ValueError("Не выпендривайтесь. Вводите числа!")
    elif int(mortgage) > 100:
        raise ValueError("Да вы совсем безбашенный")
    elif (int(mortgage) + int(life)) > 100:
        raise ValueError("А раньше головой нужно было думать, а не чем обычно")
    else:
        return f"""
            На ипотеку было потрачено: {int(int(salary) * int(mortgage) / 100 * 12)} рублей")
            Было накоплено: {int((int(salary) - int(salary) * int(mortgage) / 100 - int(salary) * int(life) / 100) * 12)} рублей
            """


if __name__ == "__main__":
    salary = input("Введите свою зарплату: ")
    mortgage = input("Введите процент по ипотеке: ")
    life = input("Введите процент на жизнь: ")
    try:
        result = savings(salary, mortgage, life)
    except ValueError as e:
        print(f"Ошибка: {e}")
    else:
        print(result)
    finally:
        print("Спасибо, работа программы завершена")
