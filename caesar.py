def rotate_character(char, rot):
    alphabet = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'
    alphabet = alphabet.split()
    rot_val = rot
    if not isinstance(rot, int):
        if rot.isnumeric():
            rot_val = int(rot)
        else:
            rot_val = alphabet_position(rot)
    if char.isupper():
        new_loc = (alphabet_position(char) + rot_val) % 26
        return alphabet[new_loc].upper()
    new_loc = (alphabet_position(char) + rot_val) % 26
    return alphabet[new_loc]

def encrypt(text, rot):
    message = ''
    for char in text:
        if char.isalpha():
            message += rotate_character(char, rot)
        else:
            message += char
       
    return message

def main():
    user_message = input('please type in a message to encrypt:')
    shift_value = int(input('please provide a number:'))
    encrypted_message = encrypt(user_message, shift_value)
    print(encrypted_message)

if __name__ == '__main__':
    main()