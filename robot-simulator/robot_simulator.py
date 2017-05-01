from collections import deque

NORTH='N'
EAST='E'
SOUTH='S'
WEST='W'

class Robot(object):
    def __init__(self, direction=NORTH, x=0, y=0):
        self.x = x
        self.y = y
        self.compass = deque('NESW')
        while self.compass[0] != direction:
            self.compass.rotate()

    def turn_right(self):
        self.compass.rotate(-1)

    def turn_left(self):
        self.compass.rotate()

    def advance(self):
        if self.bearing == NORTH:
            self.y += 1
        elif self.bearing == EAST:
            self.x += 1
        elif self.bearing == SOUTH:
            self.y -= 1
        else:
            self.x -= 1

    def simulate(self, instructions):
        for i in instructions:
            if i == 'L':
                self.turn_left()
            elif i == 'R':
                self.turn_right()
            elif i == 'A':
                self.advance()

    @property
    def bearing(self):
        return self.compass[0]

    @property
    def coordinates(self):
        return (self.x, self.y)
