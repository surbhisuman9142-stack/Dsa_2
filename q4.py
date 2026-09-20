rows = 4
triangle = []
for i in range(rows):
    row = []
    for j in range(i+1):
        if j == 0 or j == i:
            row.append(1)
        else:
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])

    triangle.append(row)
    print(*row)

    