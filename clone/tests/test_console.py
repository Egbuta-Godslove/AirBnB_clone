#!/usr/bin/python3
"""This is the module for testing the HBNBCommand Class"""
import unittest
from console import HBNBCommand
from unittest.mock import patch
from io import StringIO


class Test_Console(unittest.TestCase):
    """TThis is to test the HBNBCommand Console"""

#     def test_help(self):
#         """This tests the help commmand"""
#         with patch('sys.stdout', new=StringIO()) as f:
#             HBNBCommand().onecmd("help")
#         string = """
# Documented commands (type help <topic>):
# ========================================
# EOF  all  count  create  destroy  help  quit  show  update
# """
#         msg = f.getvalue()
#         self.assertEqual(string, msg)

    def test_help(self):
        """This tests the help command."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help")
        s = """
Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update\n
"""
        self.assertEqual(s, f.getvalue())

    # Test cases for quit

    def test_do_quit(self):
        """This tests the quit commmand"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("quit")
        # This models what happens when someone types `quit`
        msg = f.getvalue()
        self.assertTrue(len(msg) == 0)
        self.assertEqual("", msg)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("quit garbage")
        # This models when user types `quit anything`
        msg = f.getvalue()
        self.assertTrue(len(msg) == 0)
        self.assertEqual("", msg)

    # Test cases for EOF
    def test_do_EOF(self):
        """This tests the EOF commmand"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("EOF")
        # This models what happens when user types `quit`
        msg = f.getvalue()
        self.assertTrue(len(msg) == 1)
        self.assertEqual("\n", msg)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("EOF garbage")
        # This models what happens when user types `EOF anything`
        msg = f.getvalue()
        self.assertTrue(len(msg) == 1)
        self.assertEqual("\n", msg)

    # Test cases for emptyline
    def test_do_emptyline(self):
        """This tests the emptyline command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("\n")
        # This models what happens when user doesn't type anything
        msg = f.getvalue()
        self.assertTrue(len(msg) == 0)
        self.assertEqual("", msg)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("                     \n")
        # This models what happens when user types lots of whitespaces & enter
        msg = f.getvalue()
        self.assertTrue(len(msg) == 0)
        self.assertEqual("", msg)

    # Test cases for do_all
    def test_do_all(self):
        """This tests the do_all command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all")

    # Test cases for do_count
    # Test cases for do_show
    # Test cases for do_create
    # Test cases for do_update
    # Test cases for do_destroy


if __name__ == "__main__":
    unittest.main()
