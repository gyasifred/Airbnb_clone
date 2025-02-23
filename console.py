#!/usr/bin/env python3
"""
This module defines the command interpreter for HBNB.
It allows users to interact with the application using a command-line interface.
"""

import cmd
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """
    Command interpreter class for HBNB.
    Provides commands for creating, retrieving, updating, and deleting objects.
    """

    prompt = "(hbnb) "
    classes = {"BaseModel": BaseModel}

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it, and prints the id."""
        if not arg:
            print("** class name missing **")
            return
        if arg not in self.classes:
            print("** class doesn't exist **")
            return
        obj = self.classes[arg]()
        obj.save()
        print(obj.id)

    def do_show(self, arg):
        """Prints the string representation of an instance based on class name and id."""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = f"{args[0]}.{args[1]}"
        obj = storage.all().get(key)
        if not obj:
            print("** no instance found **")
        else:
            print(obj)

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id."""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = f"{args[0]}.{args[1]}"
        if key not in storage.all():
            print("** no instance found **")
            return
        del storage.all()[key]
        storage.save()

    def do_all(self, arg):
        """Prints all string representations of instances, optionally filtered by class."""
        if arg and arg not in self.classes:
            print("** class doesn't exist **")
            return
        objects = storage.all()
        obj_list = [
            f"[{obj.__class__.__name__}] ({obj.id}) {obj.__dict__}"
            for key, obj in objects.items() if not arg or key.startswith(arg + ".")
        ]
        print(obj_list)

    def do_update(self, arg):
        """Updates an instance by adding or updating an attribute."""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = f"{args[0]}.{args[1]}"
        obj = storage.all().get(key)
        if not obj:
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        attr_name, attr_value = args[2], args[3]
        try:
            if hasattr(obj, attr_name):
                attr_type = type(getattr(obj, attr_name))
                attr_value = attr_type(attr_value)
        except ValueError:
            pass
        setattr(obj, attr_name, attr_value)
        obj.save()

    def do_quit(self, arg):
        """Quit command: exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF command: exit the program."""
        print("")
        return True

    def emptyline(self):
        """Overrides default emptyline behavior (does nothing)."""
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
