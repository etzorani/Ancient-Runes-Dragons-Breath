from .character import *
		        
class NPC(Character):
    def __init(self, graphics, name, maxhp, maxmp, level, xp,
						strength, constitution, dexterity,
						intelligence, perception, learning,
						will, magic, charisma):
        Character.__init__(self, graphics, name, maxhp, maxmp, level, xp,
						strength, constitution, dexterity,
						intelligence, perception, learning,
						will, magic, charisma)