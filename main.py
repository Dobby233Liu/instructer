#!env python3

import click
import run

from _version import __version__, __program_name__

@click.command()
def main(py2_path=run.find_py2()):
	print(__program_name__)
	print("version %s" % __version__)

	print("") # newline

	print("This is working")

if __name__ == "__main__":
	main()
else:
	raise NotImplementedError()
