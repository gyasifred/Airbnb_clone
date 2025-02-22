#!/usr/bin/env python3
"""
This module contains the entry point of the command interpreter.
It uses the cmd module to implement a basic command line interface.
"""

import cmd


class HBNBCommand(cmd.Cmd):
    """
    Command interpreter class for HBNB.
    Provides commands to exit the interpreter via 'quit' or 'EOF',
    and uses a custom prompt.
    """

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """
        Quit command: exit the program.
        Usage: quit
        """
        return True

    def do_EOF(self, arg):
        """
        EOF command: exit the program.
        Usage: Ctrl-D (on *nix) or Ctrl-Z then ENTER (on Windows)
        """
        print("")  # Print a newline for a clean exit.
        return True

    def emptyline(self):
        """
        Overrides the default emptyline behavior.
        An empty line should not execute any command.
        """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
