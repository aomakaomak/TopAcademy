

ids = {'user1': [213, 213, 213, 15, 213],
       'user2': [54, 54, 119, 119, 119],
       'user3': [213, 98, 98, 35]}

# Способ 1  с рэнжом
geo_id = []

for i in range(len(ids)):
    for id in list(ids.values())[i]:
        if id not in geo_id:
            geo_id.append(id)

print(geo_id)

# Способ 2  с методом items
geo_id_new = []

for key, value in ids.items():
    for id in value:
        if id not in geo_id_new:
            geo_id_new.append(id)

print(geo_id_new)


# Способ 3 с помощью set
geo_id_new_new = []

for key, value in ids.items():
    geo_id_new_new.extend(value)
    new_set = set(geo_id_new_new)
    geo_id_new_new = list(new_set)

print(geo_id_new_new)