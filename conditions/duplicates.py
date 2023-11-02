some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
for value in some_list:

    count = some_list.count(value)
    print(value,count)
duplicates = []
for value in some_list:
    if some_list.count(value) > 1:
        if value not in duplicates:
            duplicates.append(value)

print(duplicates)