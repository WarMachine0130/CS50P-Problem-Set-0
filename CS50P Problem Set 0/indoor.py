string = list(input("Input: "))

i = 0
while i < len(string):
    if ord(string[i]) > 65 and ord(string[i]) < 90:
        string[i] = chr(ord(string[i]) + 32)
    i += 1

print(''.join(string))