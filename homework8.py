def main():
    file = open('text.txt', 'r')
    text = file.read()
    u = 0
    l = 0
    d = 0
    s = 0
    for ch in range(0, len(text)):
        if text[ch].isupper():
            u += 1
        elif text[ch].islower():
            l += 1
        elif text[ch].isdigit():
            d += 1
        elif text[ch].isspace():
            s += 1
    print('Uppercase letters:',u)
    print('Lowercase letters:',l)
    print('Digits:',d)
    print('Spaces:',s)
main()