#!env python3

import fire

def main():
  print("This is working")

if __name__ == "__main__":
  fire.Fire(main)
else:
  raise NotImplementedError()
