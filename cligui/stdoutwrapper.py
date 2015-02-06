"""Wrap stdout so that print calls can go to an io.StringIO object."""
import sys
import io

_stdout = sys.stdout

class Wrapper(io.StringIO):
    """Wrap stdout, so that print calls can go to a buffer."""

    def __init__(self, onwrite=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.onwrite = onwrite
        sys.stdout = self

    def write(self, *args, **kwargs):
        if self.onwrite:
            self.onwrite(*args, **kwargs)
        _stdout.write(*args, **kwargs)
        io.StringIO.write(self, *args, **kwargs)

    def __del__(self):
        """Put sys.stdout back in the right place."""
        sys.stdout = _stdout
