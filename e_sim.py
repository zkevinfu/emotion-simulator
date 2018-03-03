import aei
import Queue
import sys
import os
import AEIcmd
import atexit
import threading
import time

def exit_handler(obj):
    print 'Finish Exit-'
    obj.update_save()

def cmd_thread(obj,):
    global running
    prompt = AEIcmd.AEIcmd(obj)
    prompt.run()
    running = False

def weather_thread(obj,data_q):
    while running:
        pass

def main():
    if len(sys.argv) == 2:
        name = sys.argv[1]
    else:
        print 'Name of AEI?:',
        name = raw_input()

    obj = aei.aei(name)
    atexit.register(exit_handler, obj)
    command_q = Queue.Queue()
    data_q = Queue.Queue()

    in_thread = threading.Thread(target = cmd_thread, args = (obj,))
    w_thread = threading.Thread(target = weather_thread, args = (obj, data_q,))

    in_thread.start()

    obj.consume_eval(('joy', 1))
    global running
    running = True
    while running:
        if not data_q.empty():
            item = data_q.get()
    in_thread.join()
    sys.exit()

if __name__ == "__main__":
    main()
