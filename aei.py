import os
import json
import datetime
import states_obj

class aei:
    # Class variables
    states_file = 'resources/states.json'
    aei_save_path = 'aei_saves'
    with open(states_file, 'r') as f:
        state_dict = json.load(f)
    # Constructor:
    def __init__(self, name):
        """Initializes an AEI object from a given name.
        If the name exists, load data from file, if not, then create new file"""
        self.name = name
        self.save_file = '%s/%s.json'%(self.aei_save_path,name)
        # If a previous aei save does not exist under this name, create new profile
        if not os.path.exists(self.save_file):
            print 'Creating new: %s'%(self.name)
            self.last_update = datetime.datetime.now()
            # Default empotions dict initialized with value 0
            # dict.fromkeys(['x','y'], default_value) also works
            self.emotions = {
                'fear': 0,
                'anger': 0,
                'sadness': 0,
                'joy': 0,
                'disgust': 0,
                'surprise': 0,
                'trust': 0,
                'anticipation': 0
            }
            # Default emotion modifiers dictionary initialized with value 1
            self.e_mods = {
                'fear_m': 1,
                'anger_m': 1,
                'sadness_m': 1,
                'joy_m': 1,
                'disgust_m': 1,
                'surprise_m': 1,
                'trust_m': 1,
                'anticipation_m': 1
            }
            # default states set initialized with values from state_dict
            self.states = {}
            for state in self.state_dict:
                state_value = self.state_dict[state]
                self.states[state] = states_obj.states_obj( # s[state] sets a dictionaty item with a key of state
                    state_value['name'],
                    state_value['modifiers'],
                    state_value['type']
                )
            with open(self.save_file, 'w') as f:
                self_data = json.dumps(self, default = self.jdefault, indent = 2)
        # If a previous save does exist, load data from file
        else:
            print 'Loading: %s'%(self.name)
            with open(self.save_file, 'r') as f:
                self_data = json.load(f)
                self.last_update = self_data['last_update']
                self.emotions = self_data['emotions']
                self.e_mods = self_data['e_mods']
                self.states = self_data['states']
    # Datatype returner for json.dump
    def jdefault(self, o):
        if isinstance(o, datetime.datetime):
            return str(o)
        elif isinstance(o, set):
            return list(o)
        return o.__dict__
    # Writes all self data to save_file, updates last_update time
    def update_save(self):
        self.last_update = datetime.datetime.now() #may or may not want to change
        with open(self.save_file, 'w') as f:
            self_data = json.dumps(self, default = self.jdefault, indent = 2)
            f.write(self_data)
    # Method for modifying a state in an AEI obj
    def change_state(self, state, value):
        try:
            self.states[state]['level'] += value
            for modifier in self.e_mods:
                self.e_mods[modifier] += self.states[state]['modifiers'][modifier]*value
        except:
            print "SOMETHING WENT WRONG CHANGING THE STATE"
    # Takes a tuple and updates self.emotions with it
    def consume_eval(self, e_tup):
        emotion = e_tup[0]
        e_val = e_tup[1]
        self.emotions[emotion] += self.e_mods['%s_m'%emotion]*e_val
        self.emotions[emotion] = round(self.emotions[emotion], 2)
    #iterate through emotions and decay those > 0
    def decay(self):
        #TODO figure out what values i want to use
        for key in self.emotions:
            if self.emotions[key] > 0:
                self.consume_eval((key, -0.01))
                if self.emotions[key] < 0:
                    self.emotions[key] = 0
    # Print accessor methods
    def print_emotions(self):
        print '---EMOTIONS---'
        for e in self.emotions.items():
            print e
    def print_e_mods(self):
        print '---MODIFIERS---'
        for e in self.e_mods.items():
            print e
    def print_states(self):
        print '---STATES---'
        for e in self.states:
            print e
    def print_info(self):
        self.print_emotions()
        self.print_e_mods()
        self.print_states()
