#!/usr/bin/python3
''' parses markdown to html '''
import sys
from os import path


if len(sys.argv) < 2:
    print('Usage: ./markdown2html.py README.md README.html', file=sys.stderr)
elif not os.path.exists(sys.argv[1]):
    print('Missing README.md', file=sys.stderr)
else:
    exit(0)
