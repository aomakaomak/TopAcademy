

stats = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}

max_value = 0
max_key = 0

for key, value in stats.items():
    if value > max_value:
        max_value = value
        max_key = key

print(max_key)
