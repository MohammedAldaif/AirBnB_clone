#!/usr/bin/python3

import json
import cmd
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from docstrings import DocStrings

'''
entry point for the interpreter
'''


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb)"

    def do_EOF(self, line):
        ''' quit the interpreter when the user presses ctrl + d '''
        return True

    def do_quit(self, line):
        ''' quit the interpreter when the user types quit '''
        return True

    def emptyline(self):
        ''' override the original method to make it return nothing
        when the user presses enter and the input line is empty '''
        pass

    def do_help(self, arg):
        """Get help for a command.
        """
        if arg == "all":
            print(doc_string.help_all())
        elif arg == "create":
            print(doc_string.help_create())
        elif arg == "destroy":
            print(doc_string.help_destroy())
        elif arg == "show":
            print(doc_string.help_show())
        elif arg == "update":
            print(doc_string.help_update())
        else:
            super().do_help(arg)

    def do_create(self, line):
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
                    f"[{obj.__class__.__name__}] ({obj.id}){obj.to_dict()}"
                    for obj in file_storage.all().values()
                    if obj.__class__.__name__ == line
                ]
                obj_list = class_instances
            else:
                print("** class doesn't exist **")
                return
        if obj_list:
            print(obj_list)
        else:
            print("** no instance found **")

    def do_update(self, line):
        tokens = line.split()
        classes_names = globals()
        if not tokens:
            print("** class name missing **")
        elif tokens[0] not in classes_names:
            print("** class doesn't exist **")
        elif len(tokens) < 2:
            print("** instance id missing **")
        elif len(tokens) > 4:
            print("Only one attribute can be updated at a time")
        elif not self.instance_exists(tokens[0], tokens[1]):
            print("** no instance found **")
        elif len(tokens) < 3 or not tokens[2]:
            print("** attribute name missing **")
        else:
            class_name = tokens[0]
            instance_id = tokens[1]
            attribute_name = tokens[2]
            new_value = tokens[3]

            file_storage = FileStorage()
            file_storage.reload()  # Load objects from the JSON file

            key = f"{class_name}.{instance_id}"
            if key in file_storage.all():
                instance = file_storage.all()[key]
                setattr(instance, attribute_name, new_value)
            else:
                # Create a new instance with the given class and id
                cls = globals()[class_name]
                instance = cls()
                instance.id = instance_id
                setattr(instance, attribute_name, new_value)

            # Save the updated or new instance
            instance.save()

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


# Set the module docstring explicitly
__import__("console").__doc__ = """
This module defines the HBNBCommand class.
"""

if __name__ == '__main__':
    HBNBCommand().cmdloop()
