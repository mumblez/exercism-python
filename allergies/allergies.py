class Allergies(object):
    def __init__(self, allergyMask):
        self.allergies = {v: 1<<k for k, v in enumerate(['eggs', 'peanuts', 'shellfish', 'strawberries', 'tomatoes', 'chocolate', 'pollen', 'cats'])}
        self.allergyMask = allergyMask

    def is_allergic_to(self, allergy):
        return self.allergies[allergy] & self.allergyMask > 0

    @property
    def lst(self):
        return [a for a in self.allergies if self.allergies[a] & self.allergyMask > 0]

