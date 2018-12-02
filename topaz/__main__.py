import sys

import py
py.log.setconsumer("platform", None)

from topaz.main import create_entry_point


entry_point = create_entry_point()
sys.exit(entry_point(sys.argv))
