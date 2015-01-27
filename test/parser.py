"""
A test argument parser
"""

import argparse

def get_parser():
    p = argparse.ArgumentParser(description='test parser')

    p.add_argument('infile',
                   help='input file')

    p.add_argument('outfile',
                   help='output file')

    p.add_argument('-v', '--verbose',
                   help='Increase verbosity',
                   action='store_true',
                   default=False)

    return p
