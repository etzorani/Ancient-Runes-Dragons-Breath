class Grid:
    def __init__(self, grid_width, grid_height):
        self.grid_width = grid_width
        self.grid_height = grid_height

class Map:
    def __init(self, id, grid_width, grid_height, objects):
        self.grid = Grid(grid_width, grid_height)
        self.id = id
        self.objects = objects
        
    #def position_objects(self):
    #    for obj in objects:
    #        objects[obj]

class Object:
    def __init__(self, graphics):
        self.graphics = graphics
        
class Character(Object):
    def __init__(self, graphics):
        Object.__init__(self, graphics)
        
class NPC(Character):
    def __init(self, graphics):
        Character.__init__(self, graphics)
        
class MainCharacter(Character):
    def __init(self, graphics):
        Character.__init__(self, graphics, hp, mp)
        self.level = 0
        self.xp = 0
        self.hp = hp
        self.mp = mp