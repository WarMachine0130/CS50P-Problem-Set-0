string = list(input("Input: "))

i = 0
while i < len(string):
    if ord(string[i]) == 32:
        string[i] = "..."
    i += 1

print(''.join(string))