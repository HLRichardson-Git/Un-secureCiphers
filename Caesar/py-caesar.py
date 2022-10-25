def caesar(text, shift):
    result = ""

    for i in range(len(text)):
        char = text[i]

        if (char.isupper()):
            result += chr((ord(char) + shift-65) % 26 + 65)
        else:
            result += chr((ord(char) + shift-97) % 26 + 97)
    return result

text = input('Enter cipher text: ')
shift = int(input('Enter shift amount: '))

print ('Cipher Text: ' + caesar(text, shift))
