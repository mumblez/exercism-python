from collections import defaultdict

class School(object):
    def __init__(self, name):
        self.name = name
        self.grades = defaultdict(set)

    def grade(self, grade):
        return self.grades[grade]

    def add(self, student, grade):
        self.grades[grade].add(student)

    def sort(self):
        return [(grade, tuple(sorted(self.grades[grade]))) for grade in sorted(self.grades)]
