"""Tests for command line interface gui."""
from cligui import CliGui
import argparse
import operator


def get_parser():
    p = argparse.ArgumentParser(description='Add a couple numbers together; write results to stdout.')

    p.add_argument('addend1',
                   help='First number to add',
                   type=float)

    p.add_argument('addend2',
                   help='Second number to add',
                   type=float)

    p.add_argument('-m', '--multiplier',
                   help='If you want to multiply the answer...',
                   type=float,
                   default=1)

    p.add_argument('-o', '--operator',
                   help='Which operator should you use for your numbers there?',
                   choices=('+', '-', '*', '/', '**'),
                   default='+')

    p.add_argument('-v', '--verbose',
                   help='Increase verbosity',
                   action='store_true',
                   default=False)

    p.add_argument('-q', '--quiet',
                   help="Doesn't actually do anything :-(",
                   action='store_false',
                   default=True)

    formatting = p.add_argument_group('formatting')

    formatting.add_argument('-c', '--color',
                            help='The color for outputting text.',
                            choices='red green blue yellow'.split())

    formatting.add_argument('-f', '--font',
                            help='What font should the output be?',
                            choices='Times Helvetica'.split())

    return p

ops = {'+': operator.add,
       '-': operator.sub,
       '*': operator.mul,
       '/': operator.truediv,
       '**': operator.pow}


def onrun(ns):
    """
    Take the namespace and do magic with it.
    :param argparse.Namespace ns: a namespace

    :return None: doesn't do anything.
    """
    a, b, c = ns.addend1, ns.addend2, ns.multiplier
    op = ops[ns.operator]
    res = op(a, b) * c
    if ns.verbose:
        msg = ('Whenever you add {} and {} and multiply by {}, '
               'it turns out you get {}')
    else:
        msg = '({} {} {}) * {} = {}'
    print(msg.format(a, ns.operator, b, c, res))


def test_cligui():
    p = get_parser()
    gui = CliGui(p, onrun)
