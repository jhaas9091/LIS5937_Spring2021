"""Module #6 Assignment
Julie Haas
LIS 5937
Spring 2021"""

class Rectangle:
    """ A class to manufacture rectangle objects """

    def __init__(self, posn, w, h):
        """ Initialize rectangle at posn, with width w, height h """
        self.corner = posn
        self.width = w
        self.height = h

    def __str__(self):
        return "({0}, {1}, {2})".format(self.corner, self.width, self.height)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "({},{})".format(self.x, self.y)

def create_rectangle(x,y,width,height):
    """Operation: create a new instance of Rectangle
    Input parameters: x, y, width, height
    Return value: instance of Rectangle"""
    r = Rectangle(0,0,0)
    r.width = width
    r.height = height

    posn = Point()
    posn.x = x
    posn.y = y

    r.corner = posn

    #print("Rectangle created")
    return r

def str_rectangle(rect):
    """ Operation: convert given Rectangle instance into string of form (x, y, width, height)
    Input parameter: rect
    Return value: string"""

    return "Rectangle - (x,y):({}, {}), width:{}, height:{}".format(rect.corner.x, rect.corner.y, rect.width, rect.height)

def shift_rectangle(rect, dx, dy):
    """Operation: change the x and y coordinates of the given Rectangle instance
    Input parameters: rect, dx, dy
    Return value: None"""
    rect.corner.x += dx
    rect.corner.y += dy
    #print ("**Rectangle shifted to:({},{})**".format(rect.corner.x, rect.corner.y))
    return

def offset_rectangle(rect, dx, dy):
    """Operation: create a new Rectangle instance which is offset
    Input parameters: rect, dx, dy
    Return value: instance of Rectangle"""

    r = Rectangle(0,0,0)
    r.width = width
    r.height = height

    posn = Point()
    posn.x = x
    posn.y = y

    r.corner = posn

    #print("Rectangle created")
    return r

    x = rect.corner.x + dx
    y = rect.corner.y + dy
    offset = create_rectangle(x, y, rect.width, rect.height)

    #print ("**Rectangle offset**")
    return offset

box = Rectangle(Point(0, 0), 100, 200)
bomb = Rectangle(Point(100, 80), 5, 10) # In my video game
print("box: ", box)
print("bomb: ", bomb)

r1 = create_rectangle(10, 20, 30, 40)
#print("Is Instance check: ", isinstance(r1,Rectangle))
print (str_rectangle(r1))
shift_rectangle(r1, -10, -20)
print (str_rectangle(r1))
r2 = offset_rectangle(r1, 100, 100)
print (str_rectangle(r1)) # should be same as previous
print (str_rectangle(r2))

