def you_in_the_army_now(age: str, children: str, is_study: str, height: str) -> str:
    if (
        not age.isdigit()
        or not children.isdigit()
        or not height.isdigit()
        or is_study not in ["да", "нет", "Да", "Нет"]
    ):
        raise ValueError("Пожалуйста, введите корректные значения")
    height_int = int(height)
    if int(age) < 18 or int(children) >= 3 or is_study.lower() == "да":
        return "Вам повезло!  У вас отсрочка. Идите домой."
    elif 0 < height_int < 170:
        return "Вы танкист"
    elif 170 <= height_int < 180:
        return "В пехоту"
    elif 180 <= height_int < 200:
        return "В десант"
    elif height_int >= 200:
        return "Вы слишком большой. Вы не поместитесь в окоп."
    else:
        raise ValueError("Пожалуйста, введите корректные значения")


if __name__ == "__main__":
    age = input("Введите Ваш возраст: ")
    children = input("Введите количество детей: ")
    is_study = input("Учитесь ли вы?  Введите да/нет: ")
    height = input("Введите Ваш рост: ")

    try:
        result = you_in_the_army_now(age, children, is_study, height)
    except ValueError as e:
        print(f"Ошибка: {e}")
    else:
        print(result)
    finally:
        print("Спасибо, программа завершена")
