rows = 4
triangle = []
for i in range(rows):
    row = []
    for j in range(i+1):
        row.append(j + 1)
    triangle.append(row)
    print(*row)

    