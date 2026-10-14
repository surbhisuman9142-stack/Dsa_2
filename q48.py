text = "madam"
reverse = ""
for ch in text:
    reverse = ch + reverse
if text == reverse:
    print("palindrome")
else:
    print("not palindrome")
