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


def get_shop_list_by_dishes(dishes: list, person_count: int) -> dict:
    """ Считаем чего и сколько нужно купить """
    cook_book = get_ingredients_list(file_path)
    shop_dict = {}
    for dish in dishes:
        for key, value in cook_book.items():
            if key.lower() == dish.lower():
                for ingredient in value:
                    ingredient_value = {
                        'measure': ingredient['measure'],
                        'quantity': int(ingredient['quantity'])*person_count
                    }
                    if shop_dict.get(ingredient['ingredient_name']):
                        ingredient_value['quantity'] += ingredient_value['quantity']
                    shop_dict[ingredient['ingredient_name']] = ingredient_value
    return shop_dict


if __name__ == '__main__':

    file_path = 'src/lesson11/dishes.txt'
    cook_book_our = get_ingredients_list(file_path)


    print('Задание 1')
    pprint.pprint(
        cook_book_our,
        width=120,
        sort_dicts=False,
        compact=True
    )
    print('*'*20)


    dish_list = ['омлет', 'фахитос']
    person_count = 5
    shop_list = get_shop_list_by_dishes(dish_list, person_count)

    print(f'Задание 2. Считаем продукты для блюд {dish_list} на {person_count} персон.')

    pprint.pprint(
        shop_list,
        width=120,
        sort_dicts=False,
        compact=True
    )
    print('*' * 20)

