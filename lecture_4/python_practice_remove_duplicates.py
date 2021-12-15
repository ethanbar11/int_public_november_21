lst = [1, 1, 1, 2, 2, 3, 3, 3, 3, 3, 4, 5, 4, 4, 4, 3, 3, 3, 3, 1, 4, ]
new_lst = []

for value in lst:
    if value not in new_lst:
        new_lst.append(value)

print(new_lst)