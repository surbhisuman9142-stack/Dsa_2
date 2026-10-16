text = "python"
stack = []
for char in text:
    stack.append(char)
reverse = ""
while len(stack) > 0:
    reverse = reverse + stack.pop()
print(reverse)