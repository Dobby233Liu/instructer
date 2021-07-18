#!/usr/bin/env python3

import click
from .__version__ import __version__, __program_name__

@click.command()
def main():
	print(__program_name__)
	print("version %s" % __version__)

	print("") # newline

	print("This is working")

if __name__ == "__main__":
	main()
else:
	raise NotImplementedError()
