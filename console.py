#!/usr/bin/python3
import cmd
import shlex
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    ''' command interpreter to mange objects.'''

    prompt = '(hbnb) '
    inputs = ''
    classes_list = ["BaseModel"]

    def do_EOF(self, line):
        '''exit prog by pressing ctr + D'''
        return True

    def emptyline(self):
        '''Do nothing on empty line'''
        pass

    def do_quit(self, q):
        '''Quit command to exit the program'''
        return True

    def do_help(self, arg):
        '''
        Get help on commands.
        'help' or '?' with no arguments prints a list of commands.
        'help <command>' or '? <command>' gives help on <command>.
        '''
        cmd.Cmd.do_help(self, arg)

    def do_create(self, arg):
        '''creat new instance then save it to storagefile.
           USAGE: creat (class name).
        '''

        new_instance = BaseModel()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        ''' Prints the string representation of an instance.
             based on the class name and id.'''

        if len(self.inputs) < 2:
            print('** instance id missing *')
        else:
            objects = storage.all()
            key = self.inputs[0] + "." + self.inputs[1]
            if key in objects:
                print(objects[key])
            else:
                print('** no instance found **')

    def do_destroy(self, arg):
        '''  Deletes an instance based on the class name and id.
             saves the changes to the storageFile.
        '''

        if len(self.inputs) < 2:
            print('** instance id missing *')
        else:
            objects = storage.all()
            key = self.inputs[0] + "." + self.inputs[1]
            if key in objects:
                del objects[key]
                storage.save()
            else:
                print('** no instance found **')

    def do_all(self, arg):
        '''Prints all string representation of all instances
            based or not on the class name.
             Ex: $ all <class name> or $ all.'''

        objects = storage.all()
        if len(self.inputs) == 0:
            for key, val in objects.items():
                print(str(val))
        elif self.inputs[0] not in self.classes_list:
            print("** class doesn't exist **")
        else:
            for key, val in objects.items():
                if key.split('.')[0] == self.inputs[0]:
                    print(str(val))

    def do_update(self, arg):
        ''' Updates an instance based on the class name and id
             by adding or updating attribute.
        '''

        if len(self.inputs) < 2:
            print('** instance id missing *')
        else:
            objects = storage.all()
            key = self.inputs[0] + "." + self.inputs[1]
            if key not in objects:
                print("** no instance found **")
            elif len(self.inputs) < 3:
                print("** attribute name missing **")
            elif len(self.inputs) < 4:
                print("** value missing **")
            else:
                obj = objects[key]
                attr_name = self.inputs[2]
                attr_value = self.inputs[3]

                try:
                    attr_value = eval(attr_value)
                except Exception:
                    pass

                if isinstance(obj, dict):
                    obj[attr_name] = attr_value
                    print(obj)
                    obj.update()
                    '''converting to object
                    obj_instance = BaseModel(**obj)
                    setattr(obj_instance, attr_name, attr_value)
                    obj_instance.save()'''
                else:
                    setattr(obj, attr_name, attr_value)
                # storage.save()
                # print(f"Attribute '{attr_name}' updated/added successfully.")

    def precmd(self, line):
        '''Record the command that was executed. This also allows us to
         transform dashes back to underscores.
        '''
        if not line.startswith('quit') and not line.startswith('EOF'):

            (command, arg, line) = self.parseline(line)
            self.inputs = shlex.split(arg)
            if not command == 'all' and self.inputs == '':
                if len(self.inputs) == 0:
                    print('** class name missing **')
                    command = ''
                    return command
                elif self.inputs[0] not in self.classes_list:
                    print("** class doesn't exist **")
                    command = ''
                    return command

        return line


if __name__ == '__main__':
    HBNBCommand().cmdloop()
