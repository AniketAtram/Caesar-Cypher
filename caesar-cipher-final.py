# import ASCII art saved in caesar_cypher_art file
from caesar_cypher_art import intro_art
# import the corpus of text that will be used for encoding and decing the text
from letters_symbols import letters_symbols
# print the caesar cypher ASCII art when program runs
print(print(intro_art))
# save corpus in a variable for easy access
alphabets = letters_symbols


# create a function for encoding and decoding
def caesar_cypher(input_text, shift_amt, direction="encode"):
    output_text = ""
    for letter in input_text.lower():
        location = alphabets.index(letter)
        if direction == "decode":
            new_location = (location - shift_amt) % 25
            output_text += alphabets[new_location]
        else:
            new_location = (location + shift_amt) % 25
            output_text += alphabets[new_location]
    return output_text


exit_flag = False

while not exit_flag:
    print("What do you wish to do?")
    user_choice = input('Type "encode" for encoding and "decode" for decoding: ')

    if user_choice == "encode":
        plain_text = input("Enter the message to be encoded: ")
        shift = int(input("Enter the key shift value: "))
        encoded = caesar_cypher(input_text=plain_text, shift_amt=shift)
        print(f"encoded text is : {encoded}")
    else:
        direction = "decode"
        encoded_text = input("Enter the message to be decoded: ")
        shift = int(input("Enter the key shift value: "))
        decoded = caesar_cypher(input_text=encoded_text, shift_amt=shift, direction=direction)
        print(f"decoded text is : {decoded}")

    print("Do you wish to exit?")
    user_decision = input("Type 'Y' for exit 'N' to continue. ")
    if user_decision == "Y":
        exit_flag = True
