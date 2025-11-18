list_task = []

while True:
    action = input('Введите желаемое действие: add - добавить задачу, remove - удалить задачу, list - просмотреть все задачи, exit для выхода: ')
    if action == 'add':
        while True:
            task = input('Введите задачу. Для возвращения к выбору действия нажмите back: ')
            if task != 'back':
                list_task.append(task)
                print(f"Задача {task} успешно добавлена.")
                print(list_task)
            else:
                break

    elif action == 'exit':
        print('Благодарим вас за выбор нашего приложения. Программа завершена.')
        break

    elif action == 'remove':
        while True:
            try:
                remove = input('Введите номер задачи начиная с 0. Для возвращения к выбору действия нажмите back: ')
                if remove != 'back':
                    remove = int(remove)
                    list_task.pop(remove)
                    print(f"Задача {list_task[remove]} под номером {remove} успешно удалена.")
                    print(list_task)
                else:
                    break

            except IndexError as e:
                print(f'Ошибка {e}. Введите правильный номер задачи')

            except ValueError as e:
                print(f'Ошибка {e}. Вы можете ввести только число!')


    elif action == 'list':
         for index, item in enumerate(list_task):
             print(index, item)
         print('Список задач успешно выведен')

    else:
        print(f'К сожалению, вы ввели "{action}". У нас нет этого действия')
