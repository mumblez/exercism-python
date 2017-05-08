plantMap = {x[0]: x for x in 'Grass Clover Radishes Violets'.split()}
studentList = 'Alice Bob Charlie David Eve Fred Ginny Harriet Ileana Joseph Kincaid Larry'.split()
class Garden(object):

    def __init__(self, msg, students=[]):
        self.rows = msg.split('\n')
        self.students = students
        if len(self.students) > 0:
            self.students.sort()

    def plants(self, student):
        if len(self.students) == 0:
            i = studentList.index(student) * 2
        else:
            i = self.students.index(student) * 2
        return [plantMap[x[i+y]] for x in self.rows for y in range(2)]
