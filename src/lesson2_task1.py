def you_in_the_army_now(age: str, children: str, is_study: str, height: str) -> str:
    """
    Сначала проверяем, что в инпут ввели то, что нужно. Потом проверяем, что числовые значения не равны 0.
    Меньше 0 проверять смысла нет, потому что все отрицательные значения уже не прошли первую проверку на цифры.
    По той же логике нет смысла делать двойные проверки при определении рода войск, так как все плохие
    значения мы уже отсекли ранее.
    """
    if (
        not age.isdigit()
        or not children.isdigit()
        or not height.isdigit()
        or is_study.lower() not in ["да", "нет"]
    ):
        raise ValueError("Пожалуйста, введите корректные значения")
    height_int = int(height)
    if height_int == 0 or int(age) == 0:
        raise ValueError("Пожалуйста, введите корректные значения")
    if int(age) < 18 or int(children) >= 3 or is_study.lower() == "да":
        return "Вам повезло!  У вас отсрочка. Идите домой."
    elif height_int < 170:
        return "Вы танкист"
    elif height_int < 180:
        return "В пехоту"
    elif height_int < 200:
        return "В десант"
    else:
        return "Вы слишком большой. Вы не поместитесь в окоп."



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
