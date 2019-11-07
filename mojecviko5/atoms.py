import playground
import random

class Atom:
    def __init__(self,x,y,radius,speed_x,speed_y):
        self._x = x
        self._y = y
        self._radius = radius
        self._speed_x = speed_x
        self._speed_y = speed_y

    def to_tuple(self):
        result = (self._x,self._y,self._radius)
        return result

    def move(self,canvas_width,canvas_height):
        if(self._x+self._radius > canvas_width or self._x-self._radius <= 0):
            self._speed_x = self._speed_x * (-1)

        elif(self._y+self._radius > canvas_height or self._y-self._radius <= 0):
            self._speed_y = self._speed_y * (-1)   

        self._x+=self._speed_x
        self._y+=self._speed_y

class ExampleWorld(object):

    def __init__(self, size_x, size_y, numOfAtoms):
        self._width = size_x
        self._height = size_y
        self._atoms = []
        self._numOfAtoms = numOfAtoms
        for i in range(self._numOfAtoms):
            radius = random.randint(0,50)
            self._atoms.append(Atom(random.randint(radius,self._width-radius),random.randint(radius,self._height-radius),radius,2,2))

    def tick(self):
        """This method is called by playground. Sends a tuple of atoms to rendering engine.
        
        :param size_x: world size x dimension
        :param size_y: world size y dimension
        :return: tuple of atom objects, each containing (x, y, radius) coordinates 
        """
        result = []
        for i in range(self._numOfAtoms):
            self._atoms[i].move(self._width,self._height)
            result.append(self._atoms[i].to_tuple())
        return result


if __name__ == '__main__':
    size_x, size_y = 400, 300

    world = ExampleWorld(size_x, size_y, 15)
    playground.run((size_x, size_y), world)
