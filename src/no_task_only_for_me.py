# Допустим, что у нас 100 файлов. Нужен универсальный механизм
# from pathlib import Path
#
# from src.lesson11.task3 import min_number
#
#
# # получаем список названий файлов
# def get_filenames(path):
#     return [p.name for p in Path(path).iterdir() if p.is_file()]
#
#
# file_list = get_filenames("src/lesson11/files/")
#
# print(file_list)
#
# list_dict = []
#
# # формируем списки с длинами файлов, содержимом и названиями
# for document in file_list:
#     with open(f"src/lesson11/files/{document}", "r", encoding="UTF-8") as file:
#         data = file.readlines()
#     file_dict = {
#         'file_name': document,
#         'length_file': len(data),
#         'text': data
#     }
#     list_dict.append(file_dict)
#
# print(list_dict)
#
# with open("src/lesson11/files/file_common.txt", "w", encoding="UTF-8") as file:
#     file.write("")
#
# min_number = 0
# for dict in list_dict:
#     if min_number == 0 or min_number > dict.get('length_file'):
#         min_number = dict.get('length_file')
#     min_dict = list_dict.pop
#     with open("src/lesson11/files/file_common.txt", "a", encoding="UTF-8") as file:
#         file.write(min_file + "\n")
#         file.write(str(min_number) + "\n")
#         file.write("".join(min_data))


#
# # формируем конечный файл. каждый раз находим наименьший элемент в списке длин, удаляем его, узнаем его индекс и по
# # этому же индекс извлекаем значения из списков названий и текстов
# min_number = 0
# while list_dict:
#     min_number = min(len_list)
#     index_of_min_number = len_list.index(min_number)
#     len_list.pop(index_of_min_number)
#     min_data = data_list.pop(index_of_min_number)
#     min_file = path_list.pop(index_of_min_number)
#     with open("src/lesson11/files/file_common.txt", "a", encoding="UTF-8") as file:
#         file.write(min_file + "\n")
#         file.write(str(min_number) + "\n")
#         file.write("".join(min_data))
