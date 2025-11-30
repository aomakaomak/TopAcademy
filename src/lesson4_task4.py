aggregate = 1

while True:
    number = int(input("Введите число. Для завершения программы введите 0: "))
    if number == 0:
        break
    else:
        aggregate = aggregate * number**2
print(aggregate)
