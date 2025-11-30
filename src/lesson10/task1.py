


def get_name(number: str, documents: list) -> str:
    """  Выводим фамилию и имя человека по номеру документа """
    for document in documents:
        if document.get('number') == number:
            return document.get('name')
    raise ValueError("Вы ввели неверный номер документа")


def get_directory(number:str, directories: dict) -> str:
    """ Выводим номер полки по номеру документа """
    for key, value in directories.items():
        if number in value:
            return key
    raise ValueError("Вы ввели неверный номер документа")


def get_list(documents: list) -> None:
    """  Выводим в консоль список всех документов """
    if documents:
        for document in documents:
            our_list = []
            for key, value in document.items():
                our_list.append(value)
            our_string = " ".join(our_list)
            print(our_string)
    else:
        raise ValueError ("Документ не может быть пустым")


def add_document(type_of_document, number, name, directory, documents, directories):
    """ Добавляем документ в список и на полку """
    new_dict = {}
    new_dict['type'] = type_of_document
    new_dict['number'] = number
    new_dict['name'] = name
    documents.append(new_dict)

    if directory not in list(directories.keys()):
        raise ValueError ("Такая полка не существует")

    for key, value in directories.items():
        if key == directory:
            value.append(number)


    return documents, directories


def main():
    """ Главная функция, которая спрашивает, какое действие хочет совершить пользователь """
    while True:
        action = input("Введите желаемое действие: p - получить имя, s - номер полки, l - список документов, a - добавить документ, для выхода нажмите Enter ")
        if not action:
            break

        try:

            if action == 'p':
                number1 = input('Введите номер документа: ')
                people = get_name(number1, documents)
                print(people)
                break

            if action == 's':
                number2 = input('Введите номер документа: ')
                shelf = get_directory(number2, directories)
                print(shelf)
                break

            if action == 'l':
                get_list(documents)
                break

            if action == 'a':
                type_doc = input('Введите тип документа: ')
                num_doc = input('Введите номер документа: ')
                name_doc = input('Введите имя владельца: ')
                dir = input('Введите номер полки: ')
                add_doc = add_document(type_doc, num_doc, name_doc, dir, documents, directories)
                print(add_doc)
                break


        except ValueError as e:
            print(e)



if __name__ == '__main__':
    documents = [
        {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
    ]

    directories = {
        '1': ['2207 876234', '11-2'],
        '2': ['10006'],
        '3': []
    }

    main()