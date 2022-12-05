def encode(dictionary, message):
    cipher = []
    for letter in message:
        cipher.append(dictionary[letter])
    join = ', '.join(cipher)
    return join


def decode(dictionary, message):
    cipher = []
    text = []
    string = " "
    for letter in message:
        string_cp = letter.replace(',',"")
        cipher.append(string_cp)
        for key in dictionary:
            if string_cp == dictionary[key]:
                cipher.clear()
                text.append(key)

    for value in text:
        string += value

    return string.title()
