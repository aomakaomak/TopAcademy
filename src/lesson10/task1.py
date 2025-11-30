from typing import Any


def get_name(number: str, documents: list) -> str:
    """Выводим фамилию и имя человека по номеру документа"""
    for document in documents:
        if document.get("number") == number:
            return document.get("name")
    raise ValueError("Вы ввели неверный номер документа")


def get_directory(number: str, directories: dict) -> str:
    """Выводим номер полки по номеру документа"""
    for key, value in directories.items():
        if number in value:
            return key
    raise ValueError("Вы ввели неверный номер документа")


def get_list(documents: list) -> None:
    """Выводим в консоль список всех документов"""
    if documents:
        for document in documents:
            our_list = []
            for key, value in document.items():
                our_list.append(value)
            our_string = " ".join(our_list)
            print(our_string)
    else:
        raise ValueError("Документ не может быть пустым")


def add_document(type_of_document, number, name, directory, documents, directories):
    """Добавляем документ в список и на полку"""
    new_dict = {}
    new_dict["type"] = type_of_document
    new_dict["number"] = number
    new_dict["name"] = name
    documents.append(new_dict)

    if directory not in list(directories.keys()):
        raise ValueError("Такая полка не существует")

    for key, value in directories.items():
        if key == directory:
            value.append(number)

    return documents, directories


def delete_document(number: str) -> Any:
    """Удаляем документ по номеру из списка и с полки"""
    flag = False
    for document in documents:
        if document.get("number") == number:
            documents.remove(document)
            flag = True

    if flag:
        flag = False
        for key, value in directories.items():
            if number in value:
                value.remove(number)
                flag = True

    if not flag:
        raise ValueError("Документа с таким номером нет")

    return documents, directories


def move_document(number_of_doc: str, number_of_dir: str) -> Any:
    """Вводим номер документа и номер целевой полки - и документ перемещается на целевую полку"""

    flag = False
    for key, value in directories.items():
        if number_of_doc in value:
            value.remove(number_of_doc)
            flag = True
    if not flag:
        raise ValueError("Вы ввели неверный номер документа")

    if flag:
        flag = False
        for key, value in directories.items():
            if number_of_dir == key:
                directories[key].append(number_of_doc)
                flag = True

    if not flag:
        raise ValueError("Вы ввели либо неверный номер полки")

    return directories


def add_directory(number: str) -> dict:
    """Добавляем новую пустую полку с номером 'number'"""
    directories[number] = []
    return directories


def main() -> None:
    """Главная функция, которая спрашивает, какое действие хочет совершить пользователь"""
    while True:
        action = input(
            "Введите желаемое действие: p - получить имя, s - номер полки, l - список документов, a - добавить документ, d - удалить документ, m - переместить документ, as - добавить новую полку, для выхода нажмите Enter "
        )
        if not action:
            break

        try:

            if action == "p":
                number1 = input("Введите номер документа: ")
                people = get_name(number1, documents)
                print(people)
                break

            if action == "s":
                number2 = input("Введите номер документа: ")
                shelf = get_directory(number2, directories)
                print(shelf)
                break

            if action == "l":
                get_list(documents)
                break

            if action == "a":
                type_doc = input("Введите тип документа: ")
                num_doc = input("Введите номер документа: ")
                name_doc = input("Введите имя владельца: ")
                dir = input("Введите номер полки: ")
                add_doc = add_document(
                    type_doc, num_doc, name_doc, dir, documents, directories
                )
                print(add_doc)
                break

            if action == "d":
                number = input("Введите номер документа для удаления: ")
                print(delete_document(number))
                break

            if action == "m":
                number = input("Введите номер документа для перемещения: ")
                directory = input("Введите номер полки для перемещения документа: ")
                print(move_document(number, directory))
                break

            if action == "as":
                directory = input("Введите номер новой полки: ")
                print(add_directory(directory))
                break

            raise ValueError("Такой команды не существует")

        except ValueError as e:
            print(e)


if __name__ == "__main__":
    documents = [
        {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"},
    ]

    directories = {"1": ["2207 876234", "11-2"], "2": ["10006"], "3": []}

    main()
