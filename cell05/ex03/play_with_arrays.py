original_array = [2, 8, 9, 48, 8, 22, -12, 2]
new_array = []
[new_array.append(i+2) for i in original_array if i > 5]

print(original_array)
print(set(new_array))