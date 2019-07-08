string = eval(input())
unique = []
for char in string[::]:
    if char not in unique:
        unique.append(char)
print(len(unique))
