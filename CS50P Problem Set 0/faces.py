def convert(str):
    str = list(str)
    i = 0
    while i < len(str):
        if str[i] == ':':
            if str[i + 1] == ')':
                str[i] = '\U0001F600'
                str.remove(str[i + 1])
            elif str[i + 1] == '(':
                str[i] = '\U00002639'
                str.remove(str[i + 1])  
        i += 1
    return ''.join(str)
def main():
    usrString = input('Input: ')
    print(convert(usrString)) 
    
main()