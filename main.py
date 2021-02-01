#!env python3

import fire
import run

from _version import __version__, __program_name__

def main(py2_path=run.find_py2()):
	print(__program_name__)
	print("version %s" % __version__)

	print("") # newline

	print("This is working")

if __name__ == "__main__":
	fire.Fire(main)
else:
	raise NotImplementedError()
