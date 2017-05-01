from string import ascii_letters, ascii_uppercase, ascii_lowercase

def rotate(msg, cipher):
    c = cipher % 26
    rot = ascii_lowercase[c:] + ascii_lowercase[:c] + ascii_uppercase[c:] + ascii_uppercase[:c]
    return msg.translate(str.maketrans(ascii_letters, rot))
