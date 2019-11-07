import playground
import random

class Atom(object):
    def __init__(self, pos_x, pos_y, speed_x, speed_y, size, color):
        self.pos_x = float(pos_x)
        self.pos_y = float(pos_y)
        self.size = float(size)
        self.speed_x = float(speed_x)
        self.speed_y = float(speed_y)
        self.color = color

    def to_tuple(self):
        return (self.pos_x, self.pos_y, self.size, self.color)

    def move(self, width, height):
        self.pos_x += self.speed_x
        self.pos_y += self.speed_y
        if self.pos_x <= self.size or self.pos_x >= width - self.size:
            self.speed_x *= -1
        if self.pos_y <= self.size or self.pos_y >= height - self.size:
            self.speed_y *= -1
        
class FallDownAtom(Atom):
    g = 3.0
    damping =  0.8

    def move(self, width, height):
        self.speed_y += self.g
        self.pos_x += self.speed_x
        self.pos_y += self.speed_y

        if self.pos_x <= self.size or self.pos_x >= width - self.size:
            self.speed_x *= -1
        
        if self.pos_x >= width - self.size:
            self.speed_x *= -1
            self.pos_x = width - self.size 


        if self.pos_y <= self.size :
            self.speed_y *= -1

        if self.pos_y >= height - self.size:
            self.pos_y = height - self.size 
            self.speed_y *= -1
            self.speed_y *= self.damping
            self.speed_x *= self.damping

        


class ExampleWorld(object):

    def __init__(self, count, width, height):
        self.size_x = width
        self.size_y = height
        self.atoms = []
        for x in range(count):
            self.atoms.append(self.random_atom())
    
    def random_atom(self):
        choise = random.randint(0,1)
        rand_speed = random.randint(1,5)
        list_of_colors = (color for color in playground.Colors)
        if choise == 0:
            return Atom(100,100,rand_speed,rand_speed,random.randint(10,50),playground.Colors.YELLOW.value)
        elif choise == 1:
            return FallDownAtom(100,100,rand_speed,rand_speed,random.randint(10,50),playground.Colors.BLUE.value)

    def tick(self, size_x, size_y):
        ret = []
        for atom in self.atoms:
            atom.move(size_x, size_y)
            ret.append(atom.to_tuple())
        return tuple(ret)


if __name__ == '__main__':
    size_x, size_y = 400, 300
    world = ExampleWorld(10, size_x, size_y)
    playground.run((size_x, size_y), world)