plantMap = {x[0]: x for x in 'Grass Clover Radishes Violets'.split()}
studentList = 'Alice Bob Charlie David Eve Fred Ginny Harriet Ileana Joseph Kincaid Larry'.split()
class Garden(object):

    def __init__(self, msg, students=studentList):
        self.rows = msg.split('\n')
        self.students = sorted(students)

    def plants(self, student):
        i = self.students.index(student) * 2
        return [plantMap[x[i+y]] for x in self.rows for y in range(2)]
