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

import re


class HBNBCommand(cmd.Cmd):
    """
    An interactive command line interpreter

    Methods:
    - emptyline(): Does nothing when an empty line is entered.
    - parse_line(line): Parses the input line and validates inputs.
    - do_quit(): Exits the program.
    - do_EOF(): Exits the program, when the EOF signal is received
    - do_all(line): Prints all instances or instances of a specific class.
    - do_create(line): Creates a new instance with given attributes.
    - do_show(line): Prints details of a specific instance.
    - do_destroy(line): Deletes a specific instance.
    - do_update(line): Updates or add an attribute of a specific instance.
    """

    prompt = "(hbnb) "

    def emptyline(self):
        """
        Name
        ----
            emptyline

        Synopsis
        --------
            Handle an empty line or a line containing only spaces

        Description
        -----------
            This method is called when an empty line or a line with spaces is
            encountered. It performs any necessary actions or processing
            specific to empty lines.

        """
        return False

    def parse_line(
            self, line, m=False, c=False, i=False, n=False, a=False, v=False):
        """
        Tokenize the input line and perform optional checks.

        All checks are disabled by default and can be enabled by the caller.

        Args:
            line (str): The input line to be tokenized.
            m (bool): Flag to enable check for missing class.
            c (bool): Flag to enable check for class.
            i (bool): Flag to enable check for ID.
            n (bool): Flag to enable check for instance.
            a (bool): Flag to enable check for attribute.
            v (bool): Flag to enable check for value.

        Returns:
            list: Tokens extracted from the input line.
            Returns None if an error occurs.
        """
        from shlex import split

        # check for errors based on flags pass
        tokens = split(line)
        if m and line == "":
            print("** class name missing **")
        elif c and tokens[0] not in models.classes:
            print("** class doesn't exit **")
        elif i and len(tokens) < 2:
            print("** instance id missing **")
        elif n and f"{tokens[0]}.{tokens[1]}" not in models.storage.all():
            print("** no instance found **")
        elif a and len(tokens) < 3:
            print("** attribute name missing **")
        elif v and len(tokens) < 4:
            print("** value missing **")
        else:
            return tokens  # success, all checks pass

    def do_quit(self, line):
        """
        Name
        ----
            quit - exit the program

        Synopsis
        --------
            quit

        Description
        -----------
            This method is called to terminate the program ensuring
            proper cleanup and resource deallocation.
        """
        return True

    def help_quit(self):
        print(cleandoc(self.do_quit.__doc__), "\n")

    def do_EOF(self, line):
        """
        Name
        ----
            EOF - end-of-file signal

        Synopsis
        --------
            Exit the program using the appropriate keyboard shortcut

            Linux: Ctrl+D
            Windows: Ctrl+Z followed by Enter

        Description
        ----------
            This method is called when the end-of-file (EOF) signal is
            received, typically triggered by the user using the specified
            keyboard shortcuts. It allows for graceful termination of the
            program, similar to the "quit" method, ensuring proper cleanup
            and resource deallocation.

        """
        print()
        return True

    def help_EOF(self):
        print(cleandoc(self.do_EOF.__doc__), "\n")

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
            This method creates a new instance of the specified class and
            saves it to a JSON file. It then prints the ID of the newly
            created instance.

        Examples
        --------
            `create User`

            This will create a new instance of the "User" class and save it
            to the JSON file.

        Errors
        ------
            `** class name missing **`  [class name] is not given.
            `** class doesn't exit`     [class name] isn't supported
        """
        tokens = self.parse_line(line, m=True, c=True)
        if tokens:
            obj = models.classes[tokens[0]]()
            obj.save()
            print(obj.id)

    def help_create(self):
        print(cleandoc(self.do_create.__doc__), "\n")

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
            This method prints the string representation of an instance based
            on the provided class name and ID. It retrieves the instance from
            the JSON file and displays its details.

        Examples
        --------
            `show Place 1`

            This will print the details of instance with ID "1" of the "Place"
            class.

        Errors
        ------
            `** class name missing **`  [class name] is not given.
            `** class doesn't exit`     [class name] isn't supported.
            `** instance id missing **` [id] is not given.
            `** no instance found **`   The object with [id] isn't available .
        """
        tokens = self.parse_line(line, m=True, c=True, i=True, n=True)
        if tokens:
            print(models.storage.all()[f"{tokens[0]}.{tokens[1]}"])

    def help_show(self):
        print(cleandoc(self.do_show.__doc__), "\n")

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
            This method deletes an instance of the specified class based on
            the provided ID. The deletion is permanent and the change is
            saved to the JSON file.

        Examples
        --------
            `destroy City 1`

            This will delete the instance with ID "1" of the "City" class and
            save the change to the JSON file.

        Errors
        ------
            `** class name missing **`  [class name] is not given.
            `** class doesn't exit`     [class name] isn't supported.
            `** instance id missing **` [id] is not given.
            `** no instance found **`   The object with [id] isn't available .
        """
        tokens = self.parse_line(line, m=True, c=True, i=True, n=True)
        if tokens:
            models.storage.all().pop(f"{tokens[0]}.{tokens[1]}")
            models.storage.save()

    def help_destroy(self):
        print(cleandoc(self.do_destroy.__doc__), "\n")

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
            This method prints the string representation of all instances,
            optionally filtered by the provided class name. It retrieves
            the instances from the JSON file and displays their details.

        Errors
        ------
            `** class doesn't exit` [class name] isn't supported.
        """
        objs = models.storage.all().values()
        objs_list = None
        if line == "":  # all
            objs_list = [str(obj) for obj in objs]
        else:  # all [class name]
            tokens = self.parse_line(line, m=True, c=True)
            if tokens:
                objs_list = [
                    str(obj)
                    for obj in objs
                    if obj.__class__.__name__ == tokens[0]
                ]
        if objs_list:
            print(objs_list)

    def help_all(self):
        print(cleandoc(self.do_all.__doc__), "\n")

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
            This method updates an instance of the specified class based on
            the provided ID by adding or modifying an attribute.
            The change is saved to the JSON file.

        Examples
        --------
            ``update Place 1 name Lagos`

            This will update the "name" attribute of the instance with ID "1"
            of the "Place" class to "Lagos" and save the change to the JSON
            file.

        Errors
        ------
            `** class name missing **`  [class name] is not given.
            `** class doesn't exit`     [class name] isn't supported.
            `** instance id missing **` [id] is not given.
            `** no instance found **`   The object with [id] isn't available .
            `** attribute name missing **`  [attribute name] not given.
            `** value missing **`       [attribute value] not given
        """
        tokens = self.parse_line(
            line, m=True, c=True, i=True, n=True, a=True, v=True)
        if tokens:
            # convert to integer or float if possible
            try:
                tokens[3] = int(tokens[3])
            except ValueError:
                try:
                    tokens[3] = float(tokens[3])
                except ValueError:
                    pass
            # update or add the attribute and it value
            obj = models.storage.all()[f"{tokens[0]}.{tokens[1]}"]
            obj.__dict__.update({tokens[2]: tokens[3]})
            obj.save()

    def help_update(self):
        print(cleandoc(self.do_update.__doc__), "\n")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
