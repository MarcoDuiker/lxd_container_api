'''
This module contains all apps known to the API.

When adding an app, make sure that both the file name and class name are the same.

eg. `sshd.py` contains the class `sshd`.

Of course, you can add more classes, but those won't be accessible as an app.
'''


import glob
import os

modules = glob.glob(os.path.dirname(__file__)+"/*.py")
__all__ = [ os.path.basename(f)[:-3] for f in modules \
            if os.path.isfile(f) \
            and not f.endswith('__init__.py')
          ]

from . import *
