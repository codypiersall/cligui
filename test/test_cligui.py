"""Tests for command line interface gui."""
from cligui import CliGui
import argparse


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

    p.add_argument('-v', '--verbose',
                   help='Increase verbosity',
                   action='store_true',
                   default=False)

    return p


def test_cligui():
    p = get_parser()
    gui = CliGui(p)
