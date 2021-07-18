#!/usr/bin/env python3

import click

@click.command()
def main():
    print("This is working")

if __name__ == "__main__":
    main()
else:
    raise NotImplementedError()
