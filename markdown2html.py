#!/usr/bin/python3
''' parses markdown to html '''
import os
import sys

if __name__ == '__main__':

    if len(sys.argv) < 3:
        print('Usage: ./markdown2html.py README.md README.html',
              file=sys.stderr)
        exit(1)
    if os.path.isfile(sys.argv[1]) == False:
        print('Missing {}'.format(sys.argv[1]), file=sys.stderr)
        exit(1)
    else:
        print()
        exit(0)
