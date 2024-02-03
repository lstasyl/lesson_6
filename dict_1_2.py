dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 4, 'c': 5, 'd': 6}


common_keys = list(set(dict1.keys()) & set(dict2.keys()))
print(common_keys)


keys_only_in_dict1 = [key for key in dict1.keys() if key not in dict2]
print(keys_only_in_dict1)


result_dict = {key: value for key, value in dict1.items() if key not in dict2}
print(result_dict)


combined_dict = {}

for key in set(dict1.keys()) | set(dict2.keys()):
    values = [dict1.get(key), dict2.get(key)]
    values = [value for value in values if value is not None]
    
    if len(values) == 1:
        combined_dict[key] = values[0]
    else:
        combined_dict[key] = values

print(combined_dict)

