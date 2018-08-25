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
    print('got args', args)

def main():
    """This incredible function will make a GUI appear.  Remarkable!"""
    p = get_parser()
    # call cligui.CliGui with the parser, and a function that takes an
    # argparse.Namespace as its argument.
    cligui.CliGui(p, do_the_best_things)

if __name__ == '__main__':
    main()
