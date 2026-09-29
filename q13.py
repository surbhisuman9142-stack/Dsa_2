row = 5
for i in range(5):
    spaces = abs(row // 2 - i)
    stars = row - 2 * spaces
    print(" " * spaces + "*" * stars) 