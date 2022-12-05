def string(dictionary, message):
    cipher = []
    for letter in message:
        cipher.append(dictionary[letter])
    return cipher
