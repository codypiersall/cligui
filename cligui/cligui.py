"""Make a gui from a command line interface."""
import argparse
import tkinter as tk


class Frame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.pack(fill=tk.BOTH, expand=True)


class Widget(object):
    """A bridge between the GUI and the command line argument."""
    def __init__(self, action, parent):
        _bridgemap[type(action)](action, parent)


class _AppendWidget(Widget):

    def __init__(self, action, parent):
        """
        :param argparse.Action action:
        :return:
        """

    def getval(self):
        pass


class _AppendConstWidget(Widget):

    def __init__(self, action, parent):
        """
        :param argparse.Action action:
        :return:
        """

    def getval(self):
        pass


class _CountWidget(Widget):

    def __init__(self, action, parent):
        """
        :param argparse.Action action:
        :return:
        """

    def getval(self):
        pass


class _HelpWidget(Widget):

    def __init__(self, action, parent):

        """
        :param argparse.Action action:
        :return:
        """
        self.frame = tk.Frame()

    def getval(self):
        pass


class _StoreWidget(Widget):
    def __init__(self, action, parent):
        """
        :param argparse.Action action:
        :return:
        """
        self.action = action

        self.frame = tk.Frame(parent)
        self.frame.pack(side=tk.TOP)
        text = action.dest + '*:' if action.required else ':'
        self._label = tk.Label(self.frame, text=text, anchor=tk.E, width=20)
        self._label.pack(side=tk.LEFT)
        self._entry = tk.Entry(self.frame, width=30)
        self._entry.pack(side=tk.LEFT)

    def getval(self):
        textval = self._entry.get()
        print(textval)
        if self.action.type:
            return self.action.type(textval)
        else:
            return textval


class _StoreConstWidget(Widget):
    def __init__(self, action, parent):
        """
        :param argparse.Action action:
        :return:
        """

    def getval(self):
        pass


class _StoreFalseWidget(Widget):
    def __init__(self, action, parent):
        """
        :param argparse.Action action:
        :return:
        """

    def getval(self):
        pass


class _StoreTrueWidget(Widget):
    def __init__(self, action, parent):
        """
        :param argparse.Action action:
        :return:
        """
        self.frame = tk.Frame(parent)

    def getval(self):
        pass


_bridgemap = {argparse._StoreAction: _StoreWidget,
              argparse._AppendAction: _AppendWidget,
              argparse._AppendConstAction: _AppendConstWidget,
              argparse._CountAction: _CountWidget,
              argparse._HelpAction: _HelpWidget,
              argparse._StoreConstAction: _StoreConstWidget,
              argparse._StoreFalseAction: _StoreFalseWidget,
              argparse._StoreTrueAction: _StoreTrueWidget}


class CliGui(object):
    def __init__(self, parser, run=None):
        """

        :param argparse.ArgumentParser parser: parser to turn into a gui
        """
        self.parser = parser
        self.make_gui()

    def make_gui(self):
        self.root = tk.Tk()
        self.frame = Frame(self.root)
        for action in self.parser._actions:
            self.add_action(action)

        buttonframes = tk.Frame(self.frame)
        self.run = tk.Button(buttonframes, text='Run',
                            command=self.check_args)
        self.cancel = tk.Button(buttonframes, text='Cancel',
                                command=self.quit)
        self.run.pack(side=tk.LEFT)
        self.cancel.pack(side=tk.LEFT)
        buttonframes.pack()

    def check_args(self):
        print('checked out yo')

    def quit(self):
        self.frame.parent.quit()

    def show(self):
        self.root.geometry('600x400+300+300')
        self.root.mainloop()

    def add_action(self, action):
        """
        :param argparse.Action action:
        :return: None
        """
        widget = Widget(action, self.frame)


    def parse_args(self):
        return self.show()

