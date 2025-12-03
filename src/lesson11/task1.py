import pprint

def get_ingredients_list(file_path: str) -> dict:
    """ Из содержимого файла делаем словарь рецептов """

    with open (file_path, 'r', encoding='UTF-8') as file:
        data = file.readlines()

    cook_book = {}

    i = 0
    while i < len(data):
        step = int(data[i + 1])
        ingr_list = []
        for n in range(i + 2, i + 2 + step):
            row = data[n].strip().split(' | ')
            ingr_dict = {
                'ingredient_name': row[0],
                'quantity': row[1],
                'measure': row[2],
            }
            ingr_list.append(ingr_dict)

        cook_book[data[i].strip()] = ingr_list
        i = i + 2 + step

    return cook_book

if __name__ == '__main__':

    file_path = 'src/lesson11/dishes.txt'
    cook_book_our = get_ingredients_list(file_path)


    pprint.pprint(
        cook_book_our,
        width=120,
        sort_dicts=False,
        compact=True
    )

