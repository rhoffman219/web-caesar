def alphabet_position(letter):
    alphabet = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'
    alphabet = alphabet.split()
    letter = letter.lower()
    return alphabet.index(letter)

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