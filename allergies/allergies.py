class Allergies(object):
    def __init__(self, allergyMask):
        self.lst = [v for k,v in enumerate(['eggs', 'peanuts', 'shellfish', 'strawberries', 'tomatoes', 'chocolate', 'pollen', 'cats']) if 1<<k & allergyMask]

    def is_allergic_to(self, allergy):
        return allergy in self.lst
