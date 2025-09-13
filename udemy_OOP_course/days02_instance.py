class Backpack:
    def __init__( self, size, name, color ):
        self.name = name
        self.size = size
        self.color = color


class Circle:
    def __init__(self, radius, color ):
        self.radius = radius
        self.color = color

    def setRadius( self, radius ):
        self.radius = radius
    
    def area( self):
        return self.radius ** 2 * 3.14


circle = Circle( 10, 'red' )
print( circle.area())


class Backpacks:
    def __init__( self ):
        self.items = []


# 