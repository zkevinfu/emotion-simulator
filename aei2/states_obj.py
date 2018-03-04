class states_obj:
    # Constuctor
    def __init__(self, name, mod_d, state_type, level=0):
        self.name = name
        self.modifiers = mod_d
        self.type = state_type
        self.level = level

    # Redefines __str__, for printing purposes
    def __str__(self):
        return 'Name: %s\nType: %s\nModifiers: %s\nLevel: %s'%(self.name, self.type, self.modifiers, self.level)
