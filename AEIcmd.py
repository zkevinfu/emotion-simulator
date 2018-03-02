import cmd
import aei

class AEIcmd(cmd.Cmd, object):
    def __init__(self, args):
        cmd.Cmd.__init__(self)
        self.obj = args
    #def run(self):
    #    self.prompt = '> '
    #    self.cmdloop('Starting prompt...')

    def do_print(self, args):
        """TODO"""
        if len(args) == 0:
            self.obj.print_info()
        else:
            command = args
            if command == 'emotions':
                self.obj.print_emotions()
            elif command == 'states':
                self.obj.print_states()
            elif command == 'e_mods':
                self.obj.print_e_mods()
            else:
                print 'Invalid Arg'

    def do_exit(self, args):
        """Exits the program."""
        print "Begin Exit-"
        return True
