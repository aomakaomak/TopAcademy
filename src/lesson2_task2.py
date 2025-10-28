import datetime


def zodiac_signs(month: str, day: str) -> str or None:
    """
    Поскольку по условиям задачи нет ввода года от пользователя,
    то для формирования даты поставим любой високосный год (чтобы не пропустить 29 февраля)
    Будем преобразовывать вводимые пользователем данные в дату, и сравнивать даты , иначе с ума сойдешь от сравнений
    """

    if month.lower() not in [
        "январь",
        "февраль",
        "март",
        "апрель",
        "май",
        "июнь",
        "июль",
        "август",
        "сентябрь",
        "октябрь",
        "ноябрь",
        "декабрь",
    ]:
        raise ValueError("Введите корректный месяц")

    year = 2024
    if month == "январь":
        month_int = 1
    elif month == "февраль":
        month_int = 2
    elif month == "март":
        month_int = 3
    elif month == "апрель":
        month_int = 4
    elif month == "май":
        month_int = 5
    elif month == "июнь":
        month_int = 6
    elif month == "июль":
        month_int = 7
    elif month == "август":
        month_int = 8
    elif month == "сентябрь":
        month_int = 9
    elif month == "октябрь":
        month_int = 10
    elif month == "ноябрь":
        month_int = 11
    elif month == "декабрь":
        month_int = 12

    try:
        day_int = int(day)
        date_obj = datetime.datetime(year, month_int, day_int)

    except ValueError as e:
        return f"Ошибка: {e}. Попробуйте заново."
    else:
        print("Вывод:")
        if datetime.datetime(year, 1, 20) <= date_obj <= datetime.datetime(year, 2, 19):
            return "Водолей"
        elif (
            datetime.datetime(year, 2, 19) <= date_obj <= datetime.datetime(year, 3, 20)
        ):
            return "Рыбы"
        elif (
            datetime.datetime(year, 3, 21) <= date_obj <= datetime.datetime(year, 4, 20)
        ):
            return "Овен"
        elif (
            datetime.datetime(year, 4, 21) <= date_obj <= datetime.datetime(year, 5, 20)
        ):
            return "Телец"
        elif (
            datetime.datetime(year, 5, 21) <= date_obj <= datetime.datetime(year, 6, 21)
        ):
            return "Близнецы"
        elif (
            datetime.datetime(year, 6, 22) <= date_obj <= datetime.datetime(year, 7, 22)
        ):
            return "Рак"
        elif (
            datetime.datetime(year, 7, 23) <= date_obj <= datetime.datetime(year, 8, 22)
        ):
            return "Лев"
        elif (
            datetime.datetime(year, 8, 23) <= date_obj <= datetime.datetime(year, 9, 22)
        ):
            return "Дева"
        elif (
            datetime.datetime(year, 9, 23)
            <= date_obj
            <= datetime.datetime(year, 10, 22)
        ):
            return "Весы"
        elif (
            datetime.datetime(year, 10, 23)
            <= date_obj
            <= datetime.datetime(year, 11, 22)
        ):
            return "Скорпион"
        elif (
            datetime.datetime(year, 11, 23)
            <= date_obj
            <= datetime.datetime(year, 12, 22)
        ):
            return "Стрелец"
        elif (
            datetime.datetime(year, 12, 22)
            <= date_obj
            <= datetime.datetime(year, 1, 19)
        ):
            return "Козерог"


if __name__ == "__main__":
    month = input("Введите месяц: ")
    day = input("Введите день: ")
    result = zodiac_signs(month, day)
    print(result)
