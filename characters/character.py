class Character():
    def __init__(self, graphics, name, maxhp, maxmp, level, xp,
						strength, constitution, dexterity,
						intelligence, perception, learning,
						will, magic, charisma):
        self.graphics = graphics
        self.name = name
        self.maxhp = maxhp
        self.hp = maxhp
        self.maxmp = maxmp
        self.mp = maxmp
        self.level = level
        self.xp = xp
        self.strength = strength
        self.constitution = constitution
        self.dexterity = dexterity
        self.intelligence = intelligence
        self.perception = perception
        self.learning = learning
        self.will = will
        self.magic = magic
        self.charisma = charisma