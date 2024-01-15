#!/usr/bin/python3
""" Console Module that has that has  implementation for the console  """
import cmd
import shlex
import sys
import json
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.state import State
from models.city import City


class HBNBCommand(cmd.Cmd):
    ''' command interpreter to mange objects.'''

    prompt = '(hbnb) '
    inputs = ''
    classes_list = ["BaseModel", "User", "Amenity",
                    "Place", "Review", "State", "City"]

    def do_EOF(self, line):
        '''
           exit prog by pressing ctr + D
        '''
        return True

    def emptyline(self):
        '''
           Do nothing on empty line
        '''
        pass

    def do_quit(self, q):
        '''
           Quit command to exit the program
        '''
        return True

    def do_help(self, arg):
        '''
        Get help on commands.
        Usage:
            help [command]
        '''
        if arg:
            # Get help for a specific command
            doc_func = getattr(self, 'help_' + arg, None)
            if doc_func:
                doc_func()
            else:
                cmd.Cmd.do_help(self, arg)
                # print(f"No help available for '{arg}'.")
        else:
            # Display general help
            super().do_help(arg)

    def help_quit(self):
        print("Exit the program. Equivalent to 'EOF'.\n")

    def do_create(self, arg):
        '''
           create new instance then save it to storagefile.
           USAGE: create (class name).
        '''

        new_instance = eval(f"{self.inputs[0]}()")
        storage.save()
        print(new_instance.id)

    def do_show(self, arg):
        ''' Prints the string representation of an instance.
             based on the class name and id.
        '''

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
        '''
            Prints all string representation of all instances
             based or not on the class name.
             Ex: $ all <class name> or $ all.
             '''
        storage.reload()
        model_list = []
        objects = storage.all()
        if len(self.inputs) == 0:
            for key in objects:
                model_list.append(str(objects[key]))
                print(json.dumps(model_list))
        elif self.inputs[0] not in self.classes_list:
            print("** class doesn't exist **")
        else:
            for key in objects:
                model_list.append(str(objects[key]))
                print(json.dumps(model_list))

    def do_update(self, arg):
        '''
           Updates an instance based on the class name and id
           by adding or updating attribute.
           USAGE : update class name attrs
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
            if line:
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
