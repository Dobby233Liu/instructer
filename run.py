#!env python3

# This module gives wrappers to
# run unrpyc.

import os

def find_py2():
	paths = os.get_exec_path()

	for p in paths:
		for prog in ["python2", "python2.exe", "py2", "py2.exe"]:
			attempt = os.path.join(p, prog)
			if os.path.isfile(attempt):
				return attempt

	raise OSError("Can't find Python 2 in the os.get_exec_path() pool")
