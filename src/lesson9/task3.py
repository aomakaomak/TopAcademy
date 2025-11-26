
queries = [
    'смотреть сериалы онлайн',
    'новости спорта',
    'афиша кино',
    'курс доллара',
    'сериалы этим летом',
    'курс по питону',
    'сериалы про спорт'
]

words_percent = {}

length_of_queries = len(queries)

for query in queries:
    counter = 0
    query_length = query.count(" ") + 1
    if query_length in words_percent:
        counter += 1
        words_percent[query_length] += counter/length_of_queries*100
    else:
        counter = 1
        words_percent[query_length] = counter/length_of_queries*100

for key, value in words_percent.items():
    print(f'Запросов из {key} слов -- {round(value)}%.')



