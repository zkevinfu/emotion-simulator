import aei
import Queue
import sys
import os
import AEIcmd
import atexit
import threading

def exit_handler(obj):
    print 'Finish Exit-'
    obj.update_save()
#e_values = ast.literal_eval(f.readline())
def cmd_thread(obj, q):
    prompt = AEIcmd.AEIcmd(obj)
    prompt.prompt = '> '
    prompt.cmdloop('Starting prompt...')
    q.put('EXIT')

def main():
    print 'Name of AEI?:',
    name = raw_input()
    obj = aei.aei(name)
    atexit.register(exit_handler, obj)
    crossq = Queue.Queue()
    in_thread = threading.Thread(target = cmd_thread, args = (obj, crossq,))
    #in_thread.start()
    cmd_thread(obj, crossq)
    running = True
    while running:
        if crossq:
            item = crossq.get()
            if item == 'EXIT':
                running = False
    in_thread.join()
    sys.exit()

if __name__ == "__main__":
    main()
