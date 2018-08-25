cligui
======

Turn an [argparse] command line interface into a GUI.  This is a very early
version, and it only works on a not-very-large subset of what is available to
argparse.  This version can turn really simple scripts into GUIs already, but
much work needs to be done.  And alas, my interest in this faded, so I am not
planning on doing the work.

Check out [Gooey], which has a better name, is more mature, and creates a
(much) better looking user interface.

Usage
-----

Whenever I am writing a command line application, I pretty much always have
this pattern: make a function to return a parser, make a function that takes an
argparse.Namespace instance (what you get back after calling `parse_args` on an
ArgumentParser instance), and make a main function to call them both.

```python
# Does not make a GUI appear.  How tragic!
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
    """This decent function makes NO GUI APPEAR.  How mundane!"""
    p = get_parser()
    args = p.parse_args()
    do_the_best_things(args)
```

To adjust this program to use cligui, you don't have to do much.  You have to
import cligui, of course, so add this line at the top of the file:

    import cligui

And the new `main` function will look like this:

```python
def main():
    """This incredible function will make a GUI appear.  Remarkable!"""
    p = get_parser()
    # call cligui.CliGui with the parser, and a function that takes an
    # argparse.Namespace as its argument.
    cligui.CliGui(p, do_the_best_things)
```

So the whole demo is this:

```python
# Makes a GUI appear.  How fortunate!
import argparse
import cligui

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
    """This incredible function will make a GUI appear.  Remarkable!"""
    p = get_parser()
    # call cligui.CliGui with the parser, and a function that takes an
    # argparse.Namespace as its argument.
    cligui.CliGui(p, do_the_best_things)
```

That's it!  Now when the script is called, a Gui will pop up and it will be
incredible.

Requirements
------------

The only requirement is Python 3.x and tkinter, which comes with most Python
distributions.

TODO
----

* Unit tests.
* Default widgets for some of the types of `argparse.Action` types.
* Handle argument groups naturally.
* Make the GUI that pops up look better.
* Think about adding a command line option to suppress the GUI and run the
  script normally.  That could be useful.
* Write a setup.py script.  Come on, self.

[argparse]: https://docs.python.org/3/library/argparse.html
[Gooey]: https://github.com/chriskiehl/Gooey/
