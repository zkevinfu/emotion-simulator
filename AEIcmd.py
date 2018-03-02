import cmd
import aei

class AEIcmd(cmd.Cmd, object):
    #Constructor
    def __init__(self, args):
        """Initailizes a AEIcmd object with the given AEI, then initiazes the rest from Cmd"""
        cmd.Cmd.__init__(self)
        self.obj = args
    def do_print(self, args):
        """Prints out AEI information. Prints all on empty call. Availible commands:
        ['emotions', 'states', 'modifiers']"""
        if len(args) == 0:
            self.obj.print_info()
        else:
            command = args
            if command == 'emotions':
                self.obj.print_emotions()
            elif command == 'states':
                self.obj.print_states()
            elif command == 'modifiers':
                self.obj.print_e_mods()
            else:
                print 'Invalid Arg'

    def do_exit(self, args):
        """Exits the program."""
        print "Begin Exit-"
        return True
