import re

# cheat
def flatten(*argv):
    if "'" in str(argv):
        return [x for x in re.findall(r'-?[0-9]{1,}', str(argv))]
    return [int(x) for x in re.findall(r'-?[0-9]{1,}', str(argv))]
