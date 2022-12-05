import encode

Morse_Code_Dict = {'A': '.-', 'B': '-...',
                   'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-',
                   'L': '.-..', 'M': '--', 'N': '-.',
                   'O': '---', 'P': '.--.', 'Q': '--.-',
                   'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--',
                   'X': '-..-', 'Y': '-.--', 'Z': '--..',
                   '1': '.----', '2': '..---', '3': '...--',
                   '4': '....-', '5': '.....', '6': '-....',
                   '7': '--...', '8': '---..', '9': '----.',
                   '0': '-----', ', ': '--..--', '.': '.-.-.-',
                   '?': '..--..', '/': '-..-.', '-': '-....-',
                   '(': '-.--.', ')': '-.--.-'}

user_input = input("Enter text to convert into Morse Code ").upper()

encoded_string = encode.string(message=user_input, dictionary=Morse_Code_Dict)


# print(encoded_string)


def decode(message, dictionary):
    cipher = []
    text = []
    string = " "
    for letter in message:
        cipher.append(letter)
        for key in dictionary:
            if letter == dictionary[key]:
                cipher.clear()
                text.append(key)

    for value in text:
        value.lower()
        string += value

    return string.capitalize()


print(decode(encoded_string, Morse_Code_Dict))
