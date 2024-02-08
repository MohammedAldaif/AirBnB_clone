#!/usr/bin/python3

import json
import cmd
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

'''
entry point for the interpreter
'''


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb)"
    def do_EOF(self,line):
        ''' quit the interprete when the user presses ctrl + d '''
        return True
    def do_quit(self,line):
        ''' quit the interpreter when the user types quit '''
        return True
    def emptyline(self):
        ''' override the origianal method to make it return nothing
        when the user press enter and the input line is empty '''
        pass
    def do_create(self,line):
        classes_names = globals()
        if line in classes_names:
            obj = classes_names[line]()
            obj_dictionary = obj.to_dict() 
            file_storage_object = FileStorage()
            file_storage_object.new(obj)
            file_storage_object.save()
            # Print the 'id' from the saved JSON file
            with open(FileStorage._FileStorage__file_path, 'r') as json_file:
                loaded_dict = json.load(json_file)
                key = "{}.{}".format(obj.__class__.__name__, obj.id)
                if key in loaded_dict:
                    print(loaded_dict[key]['id'])
        elif not line:
            print("** class name missing **")
        elif line not in classes_names:
            print("** class doesn't exist **")
    def do_show(self,line):
        classes_names = globals()
        if line in classes_names:
            obj = classes_names[line]()
            print(obj)
if __name__ == '__main__':
    HBNBCommand().cmdloop()
