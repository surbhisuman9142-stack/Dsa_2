size = 5
for i in range(size):
    spaces = abs(size//2-i)
    stars = size - 2 * spaces
    print("" * spaces + "*"  * stars)