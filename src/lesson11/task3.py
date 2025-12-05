# Допустим, что у нас 100 файлов. Нужен универсальный механизм
from pathlib import Path


# получаем список названий файлов
def get_filenames(path):
    return [p.name for p in Path(path).iterdir() if p.is_file()]


file_list = get_filenames("src/lesson11/files/")


data_list = []
len_list = []
path_list = []

# формируем списки с длинами файлов, содержимом и названиями
for document in file_list:
    with open(f"src/lesson11/files/{document}", "r", encoding="UTF-8") as file:
        data = file.readlines()
    data_list.append(data)
    len_data = len(data)
    len_list.append(len_data)
    path_list.append(document)


with open("src/lesson11/files/file_common.txt", "w", encoding="UTF-8") as file:
    file.write("")

# формируем конечный файл. каждый раз находим наименьший элемент в списке длин, удаляем его, узнаем его индекс и по
# этому же индекс извлекаем значения из списков названий и текстов
min_number = 0
while len_list:
    min_number = min(len_list)
    index_of_min_number = len_list.index(min_number)
    len_list.pop(index_of_min_number)
    min_data = data_list.pop(index_of_min_number)
    min_file = path_list.pop(index_of_min_number)
    with open("src/lesson11/files/file_common.txt", "a", encoding="UTF-8") as file:
        file.write(min_file + "\n")
        file.write(str(min_number) + "\n")
        file.write("".join(min_data))
