#!/usr/bin/python3
''' parses markdown to html '''
import sys
from os import path

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: ./markdown2html.py README.md README.html')
        exit(1)
    if not path.isfile(sys.argv[1]):
        print('Missing {}'.format(sys.argv[1]))
        exit(1)
    else:
        print()
        exit(0)
