"""Tests for command line interface gui."""
from . import parser
from cligui import CliGui

def test_cligui():
    p = parser.get_parser()
    gui = CliGui(p)
    gui.show()

