alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def caesar(plain_text, shift_amount, cipher_direction):
    cipher_text = ""
    for letter in plain_text:
        position = alphabet.index(letter)
        if direction == "encode":
            new_position = position + shift_amount
            if new_position > 25:
                new_position = alphabet.index('a') + (new_position - 26)
        elif direction == "decode":
            new_position = position - shift_amount
            if new_position < 0:
                new_position = alphabet.index('z') - (new_position - 26)

        new_letter = alphabet[new_position]
        cipher_text += new_letter
    print(f"The text is {cipher_text}")


caesar(plain_text=text, cipher_direction=direction, shift_amount=shift)