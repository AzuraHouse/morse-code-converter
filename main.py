import MorseConverter

converter = True
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

print("Welcome to the Morse Code Converter")

while converter:
    user_choice = input("If you want to encode your message type 'encode' "
                        "or if you consider to decode it type 'decode'\n").lower()
    if user_choice == "encode":
        user_input_encode = input("Enter text to convert into Morse Code ").upper()
        encoded_string = MorseConverter.encode(message=user_input_encode, dictionary=Morse_Code_Dict)

        print(f"Your encoded message is {encoded_string}")

    elif user_choice == "decode":
        user_input_decode = input("Enter text divided by coma to convert from the Morse Code ").upper()
        empty_list = user_input_decode.split()
        decoded_string = MorseConverter.decode(message=empty_list, dictionary=Morse_Code_Dict)

        print(f"Your decoded message is {decoded_string}")

    again = input("Do you want to try it again? type 'Y' yes or 'N' for no ").lower()
    if again == "y":
        pass

    elif again == "n":
        converter = False
