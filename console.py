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
# standard library imports
import cmd

# related third party imports
from inspect import cleandoc

# local imports
import models


class HBNBCommand(cmd.Cmd):
    """
    An interactive command line interpreter

    Methods:
        do_quit: command to exit the program
        do_EOF: command to exit the program
        do_all: prints all instance or instances of a particular class
        do_create: creates an instance of a particular class
        do_show: prints an instance
        do_destroy: deletes an instance
        do_update: updates an instance
        parse_line: parses the line passed and checks for any invalid inputs
        emptyline: does nothing when an empty line + Enter is entered
    """
    prompt = "(hbnb) "

    def emptyline(self):
        """
        Name
        ----
            emptyline - handle an empty line
        Synopsis
        --------
            Called when an empty line or a line with spaces is entered
        """
        return False

    def parse_line(self, line, m=False, c=False, i=False,
                   n=False, a=False, v=False):
        """
        Tokenize the input line and perform optional checks.

        All checks are disable by defaults and will be enabled by caller.

        Args:
            line: The input line to be tokenized.
            m: Flag to enable check for missing class.
            c: Flag to enable check for class.
            i: Flag to enable check for ID.
            n: Flag to enable check for instance.
            v: Flag to enable check for attribute.
            a: Flag to enable check for value.

        Returns:
            list: Tokens extracted from the input line otherwise None
            if an error occurs.
        """
        from shlex import split

        tokens = split(line)
        if m and line == '':
            print('** class name missing **')
        elif c and tokens[0] not in models.classes:
            print("** class doesn't exit **")
        elif i and len(tokens) < 2:
            print('** instance id missing **')
        elif n and f'{tokens[0]}.{tokens[1]}' not in models.storage.all():
            print('** no instance found **')
        elif a and len(tokens) < 3:
            print('** attribute name missing **')
        elif v and len(tokens) < 4:
            print('** value missing **')
        else:
            return tokens

    def do_quit(self, line):
        """
        Name
        ----
            quit - exit the program

        Synopsis
        --------
            quit
        """
        return True

    def help_quit(self):
        print(cleandoc(self.do_quit.__doc__), '\n')

    def do_EOF(self, line):
        """
        Name
        ----
            EOF - exit the program

        Synopsis
        --------
            Ctrl+D (Linux)
            Ctrl+Z followed by Enter (Windows)
        """
        print()
        return True

    def help_EOF(self):
        print(cleandoc(self.do_EOF.__doc__), '\n')

    def do_create(self, line):
        """
        Name
        ----
            create - creates an instance of a class

        Synopsis
        --------
            create [class name]

        Description
        ----------
            Creates a new instance, saves it (to the JSON file)
            and prints the id.

            For errors refer to the ERRORS section for errors that may occur.

        Errors
        ------
            `** class name missing **`   [class name] is not given.
            `** class doesn't exit`     [class name] isn't supported
        """
        tokens = self.parse_line(line, m=True, c=True)
        if tokens:
            obj = models.classes[tokens[0]]()
            obj.save()
            print(obj.id)

    def help_create(self):
        print(cleandoc(self.do_create.__doc__), '\n')

    def do_show(self, line):
        """
        Name
        ----
            show - prints an instance

        Synopsis
        --------
            show [class name] [id]

        Description
        -----------
            Prints the string representation of an instance based on the
            class name and id.

            For errors refer to the ERRORS section for errors that may occur.

        Errors
        ------
            `** class name missing **`  [class name] is not given.
            `** class doesn't exit`     [class name] isn't supported.
            `** instance id missing **`  [id] is not given.
            `** no instance found **`   The object with [id] isn't available .
        """
        tokens = self.parse_line(line, m=True, c=True, i=True, n=True)
        if tokens:
            print(models.storage.all()[f'{tokens[0]}.{tokens[1]}'])

    def help_show(self):
        print(cleandoc(self.do_show.__doc__), '\n')

    def do_destroy(self, line):
        """
        Name
        ----
            destroy - deletes an instance

        Synopsis
        --------
            destroy [class name] [id]

        Description
        ----------
            Deletes an instance based on the class name and id
            (save the change into the JSON file).

            For errors refer to the ERRORS section for errors that may occur.

        Errors
        ------
            `** class name missing **`  [class name] is not given.
            `** class doesn't exit`     [class name] isn't supported.
            `** instance id missing **`  [id] is not given.
            `** no instance found **`   The object with [id] isn't available .

        Notes
        -----
            Instance that are deleted can't be recovered.
        """
        tokens = self.parse_line(line, m=True, c=True, i=True, n=True)
        if tokens:
            models.storage.all().pop(f'{tokens[0]}.{tokens[1]}')
            models.storage.save()

    def help_destroy(self):
        print(cleandoc(self.do_destroy.__doc__), '\n')

    def do_all(self, line):
        """
        Name
        ----
            all - prints all instance

        Synopsis
        --------
            all
            all [class name]

        Description
        -----------
            Prints all string representation of all instances based or not
            on the class name.

            For errors refer to the ERRORS section for errors that may occur.

        Errors
        ------
            `** class doesn't exit`     [class name] isn't supported.
        """
        objs = models.storage.all().values()
        objs_list = None
        if line == '':
            objs_list = [str(obj) for obj in objs]
        else:
            tokens = self.parse_line(line, m=True, c=True)
            if tokens:
                objs_list = [str(obj) for obj in objs
                             if obj.__class__.__name__ == tokens[0]]
        if objs_list:
            print(objs_list)

    def help_all(self):
        print(cleandoc(self.do_all.__doc__), '\n')

    def do_update(self, line):

        """
        Name
        ----
            update - adds or update attributes

        Synopsis
        --------
            update [class name] [id] [attribute name] [attribute value]

        Description
        -----------
            Updates an instance based on the class name and id by adding or
            updating attribute (save the change into the JSON file).

            For errors refer to the ERRORS section for errors that may occur.

        Errors
        ------
            `** class name missing **`  [class name] is not given.
            `** class doesn't exit`     [class name] isn't supported.
            `** instance id missing **`  [id] is not given.
            `** no instance found **`   The object with [id] isn't available .
            `** attribute name missing **`  [attribute name] not given.
            `** value missing **`       [attribute value] not given
        """
        tokens = self.parse_line(line, m=True, c=True, i=True,
                                 n=True, a=True, v=True)
        if tokens:
            # convert to integer or float if possible
            try:
                tokens[3] = int(tokens[3])
            except ValueError:
                try:
                    tokens[3] = float(tokens[3])
                except ValueError:
                    pass
            obj = models.storage.all()[f'{tokens[0]}.{tokens[1]}']
            obj.__dict__.update({tokens[2]: tokens[3]})
            obj.save()

    def help_update(self):
        print(cleandoc(self.do_update.__doc__), '\n')


if __name__ == '__main__':
    import sys
    if sys.stdin.isatty():  # interactive mode
        HBNBCommand().cmdloop()
    else:  # non interactive mode
        input_data = sys.stdin.read()
        HBNBCommand().onecmd(input_data)
