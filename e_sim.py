import aei
import sys
import os
import atexit

def exit_handler(obj):
    print 'Closing Program'
    obj.update_save()
#e_values = ast.literal_eval(f.readline())
def proccess_stimuli(obj):
    print 'Stimuli Type:',
    stim_type = raw_input()

def print_info(obj):
    print 'Print Info:',
    info = raw_input()
    if info == 'emotions':
        obj.print_emotions()
    elif info == 'states':
        obj.print_states()
    elif info == 'e_mods':
        obj.print_e_mods()
    elif info == 'info':
        obj.print_info()

def proccess_input(S, obj):
    if S == 'exit':
        sys.exit()
    elif S == 'print':
        print_info(obj)
    elif S == 'stimuli':
        proccess_stimuli(obj)


def main():
    print 'Name of AEI?:',
    name = raw_input()
    obj = aei.aei(name)
    atexit.register(exit_handler, obj)
    while True:
        print 'Input:',
        proccess_input(raw_input(), obj)

if __name__ == "__main__":
    main()
