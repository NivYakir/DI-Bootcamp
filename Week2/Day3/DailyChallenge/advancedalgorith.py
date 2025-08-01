# # 1
rows = 5
for i in range(rows):
    spaces = rows - i - 1
    stars = 2 * i + 1
    print(" " * spaces + "*" * stars)


for i in range(rows):
    spaces = rows - (i + 1)
    stars = i + 1
    print(" " * spaces + '*' * stars)

