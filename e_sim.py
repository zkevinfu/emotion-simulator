import aei
import queue
import sys
import os
import AEIcmd
import atexit
import threading
import locweat
import time
import tkinter

def exit_handler(obj):
    print('Finish Exit-')
    obj.update_save()

def cmd_thread(obj):
    global running
    prompt = AEIcmd.AEIcmd(obj)
    # uses sys.in instead of input, this is needed since tkinter dies otherwise
    prompt.use_rawinput = False
    prompt.run()
    running = False

def display_thread(obj):
    global running
    master = tkinter.Tk()
    for i, key in enumerate(obj.emotions):
        tkinter.Label(master, text='%s: '%key).grid(row=i, sticky=tkinter.E)
    while running:
        for i, key in enumerate(obj.emotions):
            tkinter.Label(master, text=obj.emotions[key]).grid(row=i, column = 1, sticky = tkinter.W)
        try:
            master.update_idletasks()
            master.update()
        except:
            print ('tk closed')
        time.sleep(0.1)

def decay_thread(obj):
    global running
    last_time = 0
    while running:
        if time.time() - last_time > 1:
            last_time = time.time()
            obj.decay()

def weather_thread(data_q):
    global running
    last_time = 0
    while running:
        if time.time() - last_time > 120:
            last_time = time.time()
            w_q = locweat.get_stim()
            while not w_q.empty():
                data_q.put(w_q.get())
def main():
    if len(sys.argv) == 2:
        name = sys.argv[1]
    else:
        print('Name of AEI?:', end=' ')
        name = input()

    global running
    running = True

    obj = aei.aei(name)
    atexit.register(exit_handler, obj)
    data_q = queue.Queue()

    in_thread = threading.Thread(target = cmd_thread, args = (obj,))
    w_thread = threading.Thread(target = weather_thread, args = (data_q,))
    dec_thread = threading.Thread(target = decay_thread, args = (obj,))
    dis_thread = threading.Thread(target = display_thread, args = (obj,))

    in_thread.start()
    w_thread.start()
    dec_thread.start()
    #dis_thread.start()
    display_thread(obj)
    while running:
        if not data_q.empty():
            item = data_q.get()
            obj.consume_eval(item)
    in_thread.join()
    sys.exit()

if __name__ == "__main__":
    main()
