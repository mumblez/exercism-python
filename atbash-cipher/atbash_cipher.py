import re
from string import ascii_lowercase

def encode(msg):
    msg = re.sub(r'[^\w]', '', msg).lower()
    msg = msg.translate(str.maketrans(ascii_lowercase, ascii_lowercase[::-1]))
    return ' '.join([msg[x:x+5] for x in range(0, len(msg), 5)])

def decode(msg):
    return msg.translate(str.maketrans(ascii_lowercase[::-1], ascii_lowercase)).replace(' ', '')
