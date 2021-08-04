# A python program to encrypt and decrypt message using caesar cipher


# list of alphabets in english used for reference
alphabets = list("a b c d e f g h i j k l m n o p q r s t u v w x y z a b c d e f g h i j k l m n o p q r s t u v w x y z".split(" "))


# create a start menu asking users the direction
print("Welcome to caesar cypher!")
user_inp = input("type 'encode' is you wish to encode or 'decode' to see the coded message: ")


# create a function for encryption
def encryption(input_text, shift_val):
    encrypted_text = ""
    for letter in input_text:
        location = alphabets.index(letter)
        new_location = location + shift_val
        encrypted_text += alphabets[new_location]
    return encrypted_text


def decryption(input_text, shift_val):
    decrypted_text = ""
    for letter in input_text:
        location = alphabets.index(letter)
        decrypted_text += alphabets[location - shift_val]
    return decrypted_text


if user_inp == "encode":
    text = input("Enter the text to be ciphered: ").lower()
    shift = int(input("Enter the shift value: "))
    enc_text = encryption(text, shift)
    print(f"encrypted text is {enc_text}")
elif user_inp == "decode":
    text = input("Enter the text to be ciphered: ").lower()
    shift = int(input("Enter the shift value: "))
    dec_text = decryption(text, shift)
    print(f"plain text is {dec_text}")
else:
    print("Wrong Choice, program exiting......")