from itertools import accumulate

a = int(input("a"))
b = int(input("b"))
c = int(input("c"))


d = b**2 - 4 * a * c

if a == 0:
    raise ZeroDivisionError("На ноль делить нельзя")
if d < 0:
    print("Корней нет")
elif d == 0:
    x = -b / (2 * a)
    print(x)
else:
    x1 = (-b + d ** (1 / 2)) / (2 * a)
    x2 = (-b - d ** (1 / 2)) / (2 * a)
    print(x1, x2)


# file1 = "src/lesson11/files/file1.txt"
# file2 = "src/lesson11/files/file2.txt"
#
# with open(file1, "r", encoding="UTF-8") as file:
#     data1 = file.readlines()
#
# with open(file2, "r", encoding="UTF-8") as file:
#     data2 = file.readlines()
#
# len_data1 = len(data1)
# len_data2 = len(data2)
#
# with open(file1, "r", encoding="UTF-8") as file:
#     text1 = file.read()
#
# with open(file2, "r", encoding="UTF-8") as file:
#     text2 = file.read()
#
#
# with open("src/lesson11/files/file_common.txt", "w", encoding="UTF-8") as file:
#     if len_data2 < len_data1:
#         file.write(file2 + "\n")
#         file.write(str(len_data2) + "\n")
#         file.write(text2 + "\n")
#         file.write(file1 + "\n")
#         file.write(str(len_data1) + "\n")
#         file.write(text1 + "\n")
#     else:
#         file.write(file1 + "\n")
#         file.write(str(len_data1) + "\n")
#         file.write(text1 + "\n")
#         file.write(file2 + "\n")
#         file.write(str(len_data2) + "\n")
#         file.write(text2 + "\n")
