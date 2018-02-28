import json
import aei

def jdefault(o):
    return o.__dict__
    
states = {'states': 0}

print type(states)

thing = json.dumps(states)

print type(thing)
print thing

obj = aei.aei('sim1')

s = json.dumps(obj, default=jdefault)

print type(s)
print s
