import os
import json
import datetime
import states_obj

class aei:
    #class variables
    states_file = 'resources/states.json'
    aei_save_path = 'aei_saves'
    with open(states_file, 'r') as f:
        state_dict = json.load(f)
    # constructor:
    def __init__(self, name):
        self.name = name
        self.save_file = '%s/%s.json'%(self.aei_save_path,name)
        # if a previous aei save does not exist under this name, create new profile
        if not os.path.exists(self.save_file):
            self.last_update = datetime.datetime.now()
            # default empotions dict initialized with value 0
            #dict.fromkeys(['x','y'], default_value) also works
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
            # default emotion modifiers dictionary initialized with value 1
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
            self.states = set()
            for state in self.state_dict:
                s = states_obj.states_obj(
                    state['name'],
                    state['modifiers'],
                    state['type']
                )
                self.states.add(s)
            with open(self.save_file, 'w') as f:
                self_data = json.dumps(self, default = self.jdefault, indent = 2)
        # if a previous save does exist, load data from file
        else:
            with open(self.save_file, 'r') as f:
                self_data = json.load(f)
                self.last_update = self_data['last_update']
                self.emotions = self_data['emotions']
                self.e_mods = self_data['e_mods']
                self.states = self_data['states']
    # datatype returner for json.dump
    def jdefault(self, o):
        if isinstance(o, datetime.datetime):
            return str(o)
        elif isinstance(o, set):
            return list(o)
        return o.__dict__
    # writes all self data to save_file, updates last_update time
    def update_save(self):
        self.last_update = datetime.datetime.now() #may or may not want to change
        with open(self.save_file, 'w') as f:
            self_data = json.dumps(self, default = self.jdefault, indent = 2)
            f.write(self_data)
    # method for modifying a state in an AEI obj
    def change_state(self, state, value):
        if not state in self.state_dict:
            return
        # TODO: make this work
    #print accessor methods
    def print_emotions(self):
        for e in self.emotions.items():
            print e
    def print_e_mods(self):
        for e in self.e_mods.items():
            print e
    def print_states(self):
        for e in self.states:
            print e
    def print_info(self):
        print '---EMOTIONS---'
        self.print_emotions()
        print '---MODIFIERS---'
        self.print_e_mods()
        print '---STATES---'
        self.print_states()
