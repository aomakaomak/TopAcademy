

geo_logs = [
 {'visit1': ['Москва', 'Россия']},
 {'visit2': ['Дели', 'Индия']},
 {'visit3': ['Владимир', 'Россия']},
 {'visit4': ['Лиссабон', 'Португалия']},
 {'visit5': ['Париж', 'Франция']},
 {'visit6': ['Лиссабон', 'Португалия']},
 {'visit7': ['Тула', 'Россия']},
 {'visit8': ['Тула', 'Россия']},
 {'visit9': ['Курск', 'Россия']},
 {'visit10': ['Архангельск', 'Россия']}
]


geo_logs_filtered = []
country = 'Россия'

for visit in geo_logs:
    if country in list(visit.values())[0]:
        geo_logs_filtered.append(visit)

print(geo_logs_filtered)
