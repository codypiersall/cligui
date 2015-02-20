cligui
======

Turn an [argparse] command line interface into a GUI.  This is a very early
version, so nothing is considered stable yet and it only works on a
not-very-large subset of what is available to argparse.  This version can turn
really simple scripts into GUIs already, but much work needs to be done.

Usage
-----

Whenever I am writing a command line application, I pretty much always have
this pattern: make a function to return a parser, make a function that takes an
argparse.Namespace instance (what you get back after calling `parse_args` on an
ArgumentParser instance), and make a main function to call them both.

    import argparse

    def get_parser():
        """Create a parser that does all the best things."""
        p = argparse.ArgumentParser(description='such a good program')
        p.add_argument('infile')
        p.add_argument('outfile')
        return p

    def do_the_best_things(args):
        """This does the best things.

        Note: "args" is an argparse.Namespace -- the thing you get back whenever
        you call argparse.ArgumentParser().parse_args().
        """

    def main():
        p = get_parser()
        args = p.parse_args()
        do_the_best_things(args)


To adjust this program to use cligui, you don't have to do much.  You have to
import cligui, of course, so the top of the file will look like this:

    import argparse
    import cligui

    def get_parser():

And the new `main` function will look like this:

def main():
    p = get_parser()
    # call cligui.CliGui with the parser, and a function that takes an
    # argparse.Namespace as its argument.
    cligui.CliGui(p, do_the_best_things)

That's it!  Now when the script is called, a Gui will pop up and it will be
incredible.

Requirements
------------

The only requirement is Python 3.x and tkinter, which comes with most Python
distributions.

This has only been tested on Python 3.4.  It should work with any Python 3.x,
but it will not work with Python 2.x.  It wouldn't be much work to make it
compatible, so if that becomes worthwhile at some point I may do it.  It does
not depend on any third-party packages.  If you're stuck using an older Python,
you might want to check out [Gooey], which has a better name, is more mature,
and creates a better-looking GUI.  It uses wxPython, and it looks really sleek.

TODO
----

* Unit tests.
* Default widgets for some of the types of `argparse.Action` types.
* Handle argument groups naturally.
* Make the GUI that pops up look better.
* Think about adding a command line option to suppress the GUI and run the
  script normally.  That could be useful.
* Write a setup.py script.  Come on, self.


