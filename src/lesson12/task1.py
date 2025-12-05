import csv
import os


def read_students(filename, min_age, min_average):
    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), filename)
    with open(file_path, encoding="UTF-8") as file:
        reader = csv.reader(file)
        data = list(reader)
        cleaned_data = data[1:]
    filtered_data = []
    for student in cleaned_data:
        if int(student[2]) >= int(min_age) and int(student[3]) >= int(min_average):
            filtered_data.append(student)

    result_list = []
    first_string = "|".join(data[0])
    result_list.append(first_string)
    result_list.append("-" * 30)
    for student in filtered_data:
        result_list.append("|".join(student))

    return result_list


def add_student(filename, name, surname, age, average_score):
    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), filename)
    with open(file_path, encoding="UTF-8") as file:
        data = file.readlines()

    with open(file_path, "a", encoding="UTF-8", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, surname, age, average_score])

    with open(file_path, encoding="UTF-8") as file:
        new_data = file.readlines()

    if len(new_data) == len(data) + 1:
        return "Новый студент успешно добавлен!"
    else:
        return "Ошибка: студент не был добавлен!"


def main():

    try:
        while True:
            user_choice = input(
                "Введите желаемое действие: r - отфильтровать студентов, w - добавить новую запись. Для выхода нажмите Enter: "
            )
            if not user_choice:
                break
            if user_choice == "r":
                file_name = input("Введите имя файла: ")
                min_age = input("Введите минимальный возраст: ")
                if not min_age.isdigit():
                    raise ValueError("Возраст должен быть числом!")
                min_average = input("Введите минимальный средний балл: ")
                if not min_average.isdigit():
                    raise ValueError("Средний балл должен быть числом!")
                result = read_students(file_name, min_age, min_average)
                for row in result:
                    print(row)
                break
            if user_choice == "w":
                file_name = input("Введите имя файла: ")
                name_student = input("Введите имя: ")
                if not name_student.isalpha():
                    raise ValueError("Имя должно состоять только из букв")
                surname_student = input("Введите фамилию: ")
                if not surname_student.isalpha():
                    raise ValueError("Фамилия должна состоять только из букв")
                age_student = input("Введите возраст: ")
                if not age_student.isdigit():
                    raise ValueError("Возраст должен быть числом!")
                score_student = input("Введите средний балл: ")
                if not score_student.isdigit():
                    raise ValueError("Средний балл должен быть числом!")

                print(
                    add_student(
                        file_name,
                        name_student,
                        surname_student,
                        age_student,
                        score_student,
                    )
                )
                break

            raise ValueError("Такой опции нет")

    except ValueError as e:
        print(e)

    except FileNotFoundError as e:
        print(e)


if __name__ == "__main__":

    main()
