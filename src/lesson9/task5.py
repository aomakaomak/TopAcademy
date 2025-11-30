our_list = ["2018-01-01", "yandex", "cpc", 100]

final_result = {"2018-01-01": {"yandex": {"cpc": 100}}}


new_new_dict = {}
new_new_new_dict = {}

new_dict = {}

# пока только так, не могу додуматься, как нормально сделать. еще подумаю


end_range = -len(our_list)
print(end_range)
for i in range(-1, end_range, -1):
    if new_dict == {}:
        new_dict[our_list[i - 1]] = our_list[i]
    elif new_new_dict == {}:
        new_new_dict[our_list[i - 1]] = new_dict
    elif new_new_new_dict == {}:
        new_new_new_dict[our_list[i - 1]] = new_new_dict
print(new_new_new_dict)
