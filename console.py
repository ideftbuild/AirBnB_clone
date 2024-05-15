#!/usr/bin/env python3
"""
HBNBCommand Module

This module defines the HBNBCommand class, which represents a command-line
interpreter for the HBNB project. The interpreter allows users to interact
with the HBNB application through the command line, executing various commands
related to property management.

Example:
    To run the script and launch the HBNB command-line interpreter:
    ```
    python console.py
    ```

Key Features:
    - Supports various commands for managing HBNB properties.
    - Provides an interactive command-line interface for user interaction.

Notes:
    - Ensure that the necessary dependencies and configurations are in place
    before running the script.
    - Refer to the HBNB documentation for a list of available commands and
    their usage.
"""

import cmd
from inspect import cleandoc


class HBNBCommand(cmd.Cmd):
    """
    An interactive command line interpreter

    Methods:
        do_quit: command to exit the program
        do_EOF: command to exit the program
        emptyline: does nothing when an empty line + Enter is entered
    """
    prompt = "(hbnb) "

    def do_quit(self, line):
        """
        NAME
            quit - exit the program

        SYNOPSIS
            quit
        """
        return True

    def help_quit(self):
        print(cleandoc(self.do_quit.__doc__), '\n')

    def do_EOF(self, line):
        """
        NAME
            EOF - exit the program

        SYNOPSIS
            Ctrl+D (Linux)
            Ctrl+Z followed by Enter (Windows)
        """
        print()
        return True

    def help_EOF(self):
        print(cleandoc(self.do_EOF.__doc__), '\n')

    def emptyline(self):
        """
        NAME
            emptyline - handle an empty line
        SYNOPSIS
            Called when an empty line or a line with spaces is entered
        """
        return False


if __name__ == '__main__':

    import sys
    if sys.stdin.isatty():
        HBNBCommand(stdin=input).cmdloop()
    else:
        input_data = sys.stdin.read()
        HBNBCommand().onecmd(input_data)
