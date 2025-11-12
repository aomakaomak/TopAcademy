start = 1
end = int(input("Введите число: "))

print('Фигура А')
for i in range(start, end):
    print('*' * i)

print('-' * 10)

print('Фигура Б')
for i in range((end-1), (start-1), -1):
    print((' ' * (end-(i+1))) + ('*' * i))

print('-' * 10)


print('Фигура В')
for i in range(start, end):
    if i <= end/2:
        print(('*' * i) + (' ' * (end - i * 2)) + ('*' * i))
    else:
        print('*' * (end))

print('-' * 10)


print('Фигура Г')
for i in range(start, end):
    if i <= end/2:
        print('*' * (end))
    else:
        print(('*' * (int(end/2)-(i-int(end/2)))) + (' ' * (end - 2*(int(end/2)-(i-int(end/2))))) +  ('*' * (int(end/2)-(i-int(end/2)))) )

print('-' * 10)


print('Фигура Д')
for i in range(start, end):
    if i <= end/2:
        print(('*' * i) + (' ' * (end - i * 2)) + ('*' * i))
    else:
        print(('*' * (int(end/2)-(i-int(end/2)))) + (' ' * (end - 2*(int(end/2)-(i-int(end/2))))) +  ('*' * (int(end/2)-(i-int(end/2)))) )

print('-' * 10)


print('Фигура Е')

if end % 2 == 1:
    end_ = end - 1
    for i in range(start, end_):
        if i < int(end/2):
            print((' ' * (i-1)) + ('*' * (end - i * 2)) + (' ' * (i-1)))
        else:
            print((' ' * (int(end/2)-(i+1-int(end/2)))) + ('*' * (end - 2*(int(end/2)-(i-int(end/2))))) +  (' ' * (int(end/2)-(i+1-int(end/2)))) )
else:
    end_ = end
    for i in range(start, end_):
        if i < int(end/2):
            print((' ' * (i-1)) + ('*' * (end - i * 2)) + (' ' * (i-1)))
        elif i == int(end/2):
            pass
        else:
            print((' ' * (int(end/2)-(i+1-int(end/2)))) + ('*' * (end - 2*(int(end/2)-(i-int(end/2))))) +  (' ' * (int(end/2)-(i+1-int(end/2)))) )

print('-' * 10)


print('Фигура Ж')

if end % 2 == 1:
    end_ = end - 1
    for i in range(start, end_):
        if i < int(end/2):
            print((' ' * (i-1)) + ('*' * (end - i * 2)) + ('*' * (i-1)))
        else:
            print((' ' * (int(end/2)-(i+1-int(end/2)))) + ('*' * (end - 2*(int(end/2)-(i-int(end/2))))) +  ('*' * (int(end/2)-(i+1-int(end/2)))) )
else:
    end_ = end
    for i in range(start, end_):
        if i < int(end/2):
            print((' ' * (i-1)) + ('*' * (end - i * 2)) + ('*' * (i-1)))
        elif i == int(end/2):
            pass
        else:
            print((' ' * (int(end/2)-(i+1-int(end/2)))) + ('*' * (end - 2*(int(end/2)-(i-int(end/2))))) +  ('*' * (int(end/2)-(i+1-int(end/2)))) )

print('-' * 10)


print('Фигура З')

if end % 2 == 1:
    end_ = end - 1
    for i in range(start, end_):
        if i < int(end/2):
            print(('*' * (i-1)) + ('*' * (end - i * 2)) + (' ' * (i-1)))
        else:
            print(('*' * (int(end/2)-(i+1-int(end/2)))) + ('*' * (end - 2*(int(end/2)-(i-int(end/2))))) +  (' ' * (int(end/2)-(i+1-int(end/2)))) )
else:
    end_ = end
    for i in range(start, end_):
        if i < int(end/2):
            print(('*' * (i-1)) + ('*' * (end - i * 2)) + (' ' * (i-1)))
        elif i == int(end/2):
            pass
        else:
            print(('*' * (int(end/2)-(i+1-int(end/2)))) + ('*' * (end - 2*(int(end/2)-(i-int(end/2))))) +  (' ' * (int(end/2)-(i+1-int(end/2)))) )

print('-' * 10)


print('Фигура И')
for i in range(start, end):
    print((' ' * (end-(i+1))) + ('*' * i))

print('-' * 10)

print('Фигура К')
for i in range((end-1), (start-1), -1):
    print('*' * i)
