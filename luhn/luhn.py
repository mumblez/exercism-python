import re

class Luhn(object):
    def __init__(self, cc):
        self.invalid = any(re.findall(r'[^ 0-9]+', cc))
        if self.invalid:
            return

        self.cc = [int(x) for x in cc.replace(' ', '')]
        self.total = sum(self.cc[-1::-2])
        for digit in self.cc[-2::-2]:
            if digit*2 > 9:
                self.total += (digit*2) - 9
            else:
                self.total += digit*2

    def is_valid(self):
        if self.invalid:
            return False
        if len(self.cc) < 2:
            return False
        if self.total % 10 != 0:
            return False
        return True
