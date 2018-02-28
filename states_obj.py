import json

# constructor
class states_obj:
    def __init__(self, name, mod_d, state_type, level=0):
        self.name = name
        self.modifiers = mod_d
        self.type = state_type
        self.level = level
    def jdefault(self, o):
        return o.__dict__

    def print_info(self):
        print self.name
        print self.mod_d
        print self.state_type
        print self.level
