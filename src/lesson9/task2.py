

ids = {'user1': [213, 213, 213, 15, 213],
       'user2': [54, 54, 119, 119, 119],
       'user3': [213, 98, 98, 35]}

# Способ 1
geo_id = []

for i in range(len(ids)):
    for id in list(ids.values())[i]:
        if id not in geo_id:
            geo_id.append(id)

print(geo_id)

# Способ 2
geo_id_new = []

for index, value in ids.items():
    for id in value:
        if id not in geo_id_new:
            geo_id_new.append(id)

print(geo_id_new)


geo_id_new_new = []

for index, value in ids.items():
    geo_id_new_new.extend(value)

print(geo_id_new_new)