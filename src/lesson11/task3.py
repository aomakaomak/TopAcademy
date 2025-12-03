file1 = 'src/lesson11/files/file1.txt'
file2 = 'src/lesson11/files/file2.txt'

with open (file1, 'r', encoding='UTF-8') as file:
    data1 = file.readlines()

with open (file2, 'r', encoding='UTF-8') as file:
    data2 = file.readlines()

len_data1 = len(data1)
len_data2 = len(data2)

with open (file1, 'r', encoding='UTF-8') as file:
    text1 = file.read()

with open (file2, 'r', encoding='UTF-8') as file:
    text2 = file.read()

print(text1)
print(text2)


with open ('src/lesson11/files/file3.txt', 'w', encoding='UTF-8') as file:
    if len_data2 < len_data1:
        file.write(file2 + '\n')
        file.write(str(len_data2) + '\n')
        file.write(text2 + '\n')
        file.write(file1 + '\n')
        file.write(str(len_data1) + '\n')
        file.write(text1 + '\n')
    else:
        file.write(file1 + '\n')
        file.write(str(len_data1) + '\n')
        file.write(text1 + '\n')
        file.write(file2 + '\n')
        file.write(str(len_data2) + '\n')
        file.write(text2 + '\n')
