"""Make a gui from a command line interface."""
import argparse
import tkinter as tk
from tkinter import ttk
from .stdoutwrapper import Wrapper
from collections import OrderedDict


class Frame(tk.Frame):
    """A Frame with some cool defaults. (that can be overwridden)"""
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        fill = kwargs.get('fill', tk.BOTH)
        expand = kwargs.get('expand', True)
        pady = kwargs.get('pady', 3)
        self.parent = parent
        self.pack(fill=fill, expand=expand, pady=pady)


class Widget(object):
    """A bridge between the GUI and the command line argument."""

    # The entry for a thing.
    ENTRY_WIDTH = 30

    def __init__(self, action, parent):
        """
        :param argparse.Action action:
        :param tk.Frame parent:
        :return:
        """

        self.action = action
        self.frame = Frame(parent)
        self.frame.pack(side=tk.TOP)
        self.__class__ = _widgetmap[type(action)]

    def _dolabel(self):
        text = self.action.dest + ('*:' if self.action.required else ':')
        self._label = tk.Label(self.frame, text=text, anchor=tk.E, width=10)
        self._label.pack(side=tk.LEFT)

    def _dohelp(self):
        self._help = tk.Label(self.frame, text=self.action.help, anchor=tk.W, width=30)
        self._help.pack(side=tk.LEFT)


class _AppendWidget(Widget):

    def __init__(self, action, parent):
        """
        :param argparse.Action action:
        :return:
        """
        super().__init__(action, parent)

    def getval(self):
        pass


class _AppendConstWidget(Widget):

    def __init__(self, action, parent):
        """
        :param argparse.Action action:
        :return:
        """
        super().__init__(action, parent)

    def getval(self):
        pass


class _CountWidget(Widget):

    def __init__(self, action, parent):
        """
        :param argparse.Action action:
        :return:
        """
        super().__init__(action, parent)
        self._dolabel()
        tk.Listbox(self.frame, width=self.ENTRY_WIDTH)

    def getval(self):
        pass


class _HelpWidget(Widget):

    def __init__(self, action, parent):

        """
        :param argparse.Action action:
        :return:
        """
        super().__init__(action, parent)

    def getval(self):
        pass


class _StoreWidget(Widget):
    def __init__(self, action, parent):
        """
        :param argparse.Action action:
        :return:
        """
        super().__init__(action, parent)
        self._dolabel()
        if action.choices:
            self._entry = ttk.Combobox(self.frame, state='readonly', width=self.ENTRY_WIDTH)
            self._entry['values'] = action.choices
            self._entry.pack(side=tk.LEFT)
            if action.default and action.default in action.choices:
                self._entry.current(action.choices.index(action.default))

        else:
            self._entry = tk.Entry(self.frame, width=self.ENTRY_WIDTH)
            self._entry.pack(side=tk.LEFT)
            if action.default:
                self._entry.insert(0, str(action.default))
        self._dohelp()

    def getval(self):
        textval = self._entry.get()
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
        super().__init__(action, parent)

    def getval(self):
        pass

class _StoreBoolWidget(Widget):
    def __init__(self, action, parent):
        """
        :param argparse.Action action:
        :return:
        """
        super().__init__(action, parent)
        self._dolabel()
        self.state = tk.IntVar()
        self.cb = tk.Checkbutton(self.frame, width=30, anchor=tk.W, variable=self.state)
        self.cb.pack(side=tk.LEFT)
        self._dohelp()

    def getval(self):
        return self.state.get()


class _StoreTrueWidget(_StoreBoolWidget):
    def __init__(self, action, parent):
        """
        :param argparse.Action action:
        :return:
        """
        super().__init__(action, parent)


class _StoreFalseWidget(_StoreBoolWidget):
    def __init__(self, action, parent):
        """
        :param argparse.Action action:
        :return:
        """
        super().__init__(action, parent)
        self.cb.select()

    def getval(self):
        pass



_widgetmap = {argparse._StoreAction: _StoreWidget,
              argparse._AppendAction: _AppendWidget,
              argparse._AppendConstAction: _AppendConstWidget,
              argparse._CountAction: _CountWidget,
              argparse._HelpAction: _HelpWidget,
              argparse._StoreConstAction: _StoreConstWidget,
              argparse._StoreFalseAction: _StoreFalseWidget,
              argparse._StoreTrueAction: _StoreTrueWidget}


class CliGui(object):
    """Turn a command line script into a GUI.  It's pretty ugly, but effective."""
    def __init__(self,
                 parser, onrun, show=True):
        """
        :param argparse.ArgumentParser parser: parser to turn into a gui

        :param callable onrun: callable to run when the run button is pressed.
          The callable must take an argparse.Namespace as its only argument.
        :param bool show: Whether to show the GUI by default.  The only use case
          for this to be False is for testing.
        """
        self.parser = parser
        self.onrun = onrun
        self.widgets = OrderedDict()
        self.make_gui()
        self.stdout = Wrapper(self.onwrite)
        if show:
            self.show()

    def make_gui(self):
        self.root = tk.Tk()
        self.frame = Frame(self.root)
        for action in self.parser._actions:
            self.widgets[action] = self.add_action(action)

        # add run and cancel buttons.
        buttonframes = tk.Frame(self.frame)
        self.run = tk.Button(buttonframes, text='Run',
                            command=self.parse_args)
        self.cancel = tk.Button(buttonframes, text='Cancel',
                                command=self.quit)
        self.run.pack(side=tk.LEFT)
        self.cancel.pack(side=tk.LEFT)
        buttonframes.pack()

        # add stdout wrapper
        self.stdoutframe = Frame(self.frame)

        self.entry = tk.Text(self.stdoutframe)
        self.entry.configure(state='disabled')
        self.entry.pack(fill=tk.BOTH)

    def onwrite(self, text):
        self.entry.configure(state='normal')
        self.entry.insert(tk.END, text)
        self.entry.configure(state='disabled')

    def parse_args(self):
        ns = argparse.Namespace()
        for action, widget in self.widgets.items():
            if isinstance(widget, _HelpWidget):
                continue
            val = widget.getval()
            setattr(ns, widget.action.dest, val)

        if self.onrun:
            self.onrun(ns)
            print('-' * 25)
            print()
        return ns

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
        widget = _widgetmap[type(action)](action, self.frame)
        return widget
