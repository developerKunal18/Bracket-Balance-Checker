expression = input("Enter expression: ")

stack = []
pairs = {')': '(', ']': '[', '}': '{'}

balanced = True

for char in expression:
    if char in "([{":
        stack.append(char)
    elif char in ")]}":
        if not stack or stack[-1] != pairs[char]:
            balanced = False
            break
        stack.pop()

if balanced and not stack:
    print("Balanced")
else:
    print("Not Balanced")
