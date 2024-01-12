#!/usr/bin/python3
import cmd


class HBNBCommand(cmd.Cmd):
    ''' command interpreter to mange objects.'''

    prompt = 'hbnb'

    def do_EOF(self, line):
        '''exit prog by pressing ctr + D'''
        return True

    def emptyline(self):
        '''Do nothing on empty line'''
        pass

    def do_quit(self, q):
        '''Quit command to exit the program'''
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
