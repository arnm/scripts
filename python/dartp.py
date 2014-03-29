#!/usr/bin/env python
""" dartp.

Usage:
    dartp.py new <name> [<directory>]

Options:
    -h --help    Show help message.
    -v --version Show version.
"""

from docopt import docopt
import os


def new(name, root='.'):
    root = os.path.join(root, name)

    pubspec_content = "name: %s\ndependencies:\n\tbrowser: any\n" % (name)
    files = {'pubspec.yaml': pubspec_content}
    directories = ['lib', 'web']

    for directoryname in directories:
        directory = os.path.join(root, directoryname)
        if not os.path.exists(directory):
            os.makedirs(directory)

    for filename in files:
        f = os.path.join(root, filename)
        if not os.path.exists(f):
            with open(f, 'w') as fh:
                fh.write(files[filename])

def run(args):
    if args['new']:
        if args['<directory>']:
            new(args['<name>'], args['<directory>'])
            return
        else:
            new(args['<name>'])
            return

if __name__ == '__main__':
    args = docopt(__doc__, version='dartp 0.0.1')
    run(args)
