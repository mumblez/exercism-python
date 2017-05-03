import re
from math import ceil
from string import ascii_lowercase

def encode(msg):
    msg = re.sub(r'[^\w]', '', msg).lower()
    msg = msg.translate(str.maketrans(ascii_lowercase, ascii_lowercase[::-1]))
    return ' '.join([msg[5*x-5:5*x] for x in range(1, ceil(len(msg)/5) +1)])

def decode(msg):
    return msg.translate(str.maketrans(ascii_lowercase[::-1], ascii_lowercase)).replace(' ', '')
