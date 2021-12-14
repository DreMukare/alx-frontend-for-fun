#!/usr/bin/python3
''' parses markdown to html '''
import sys
from os import path


if len(sys.argv) < 2:
    print('Usage: ./markdown2html.py README.md README.html', file=sys.stderr)
    exit(1)
elif not path.exists(sys.argv[1]):
    print('Missing README.md', file=sys.stderr)
    exit(1)
else:
    exit(0)
