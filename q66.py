def is_valid(s):
    stack = []
    matching = {
        ')' : '(',
        '}' : '{',
        ']' : '['
    }
    for char in s:
        if char in "({[":
            stack.append(char)
        else:
            if len(stack) == 0:
                return False
            top = stack.pop()
            if top != matching[char]:
                return False
    return len(stack) == 0
print(is_valid("()[]{}"))
print(is_valid("([)]"))
print(is_valid("{[]}"))       