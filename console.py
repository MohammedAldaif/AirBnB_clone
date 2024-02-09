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
    def do_show(self, line):
        tokens = line.split()
        classes_names = globals()

        if not tokens:
            print("** class name missing **")
        elif tokens[0] not in classes_names:
            print("** class doesn't exist **")
        elif len(tokens) < 2:
            print("** instance id missing **")
        elif tokens[0] in classes_names:
            file_storage = FileStorage()
            file_storage.reload()  # Load objects from the JSON file

            obj_dict = file_storage.all().get(f"{tokens[0]}.{tokens[1]}", None)
            if obj_dict:
                print(obj_dict)
            else:
                print("** no instance found **")
    def do_destroy(self, line):
        tokens = line.split()
        classes_names = globals()

        if not tokens:
            print("** class name missing **")
        elif tokens[0] not in classes_names:
            print("** class doesn't exist **")
        elif len(tokens) < 2:
            print("** instance id missing **")
        elif tokens[0] in classes_names:
            file_storage = FileStorage()
            file_storage.reload()  # Load objects from the JSON file

            obj_dict = file_storage.all().get(f"{tokens[0]}.{tokens[1]}", None)
            if obj_dict:
                key = f"{tokens[0]}.{tokens[1]}"
                del file_storage.all()[key]
                file_storage.save()
            else:
                print("** no instance found **")
    def do_all(self, line):
        file_storage = FileStorage()
        file_storage.reload()  # Load objects from the JSON file

        if not line:
            # If no class name is provided, print all instances
            obj_list = list(file_storage.all().values())
        else:
            # If a class name is provided, filter instances by class name
            classes_names = globals()
            if line in classes_names:
                class_instances = [
                    obj.to_dict() for obj in file_storage.all().values()
                    if obj.__class__.__name__ == line
                ]
                obj_list = class_instances
            else:
                print("** class doesn't exist **")
                return

        if obj_list:
            for obj_dict in obj_list:
                print(str(obj_dict))
        else:
            print("** no instance found **")
    def do_update(self,line):
        tokens = line.split()
        classes_names = globals()
        if not tokens:
            print("** class name missing **")
        elif tokens[0] not in classes_names:
            print("** class doesn't exist **")
        elif len(tokens) < 2:
            print("** instance id missing **")
        elif len(tokens) > 4:
            print("Only one attribute can be updated at the time")
        elif not self.instance_exists(tokens[0],tokens[1]):
            print("** no instance found **")
        elif len(tokens) < 3 or not tokens[2]:
            print("** attribute name missing **")
        file_storage = FileStorage()
        file_storage.reload()  # Load objects from the JSON file
    def instance_exists(self, class_name, obj_id):
        """
        Check if an instance of the given class and ID exists.
        """
        file_storage = FileStorage()
        file_storage.reload()
        key = f"{class_name}.{obj_id}"
        return key in file_storage.all()
    def attribute_exists(self, class_name, attribute_name):
        """
        Check if the attribute exists in the JSON file for the given class.
        """
        file_storage = FileStorage()
        file_storage.reload()
        instances = file_storage.all().values()

        for instance in instances:
            if (
                instance.__class__.__name__ == class_name
                and hasattr(instance, attribute_name)
            ):
                return True

        return False
if __name__ == '__main__':
    HBNBCommand().cmdloop()
