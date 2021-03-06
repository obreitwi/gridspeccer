#!/usr/bin/env python2
# encoding: utf-8

import argparse
import glob
import matplotlib as mpl
import os
import os.path as osp
import sys

sys.path.insert(0, osp.dirname(osp.abspath(__file__)))

from . import core
from .core import log


def plot():
    parser = argparse.ArgumentParser(prog='gridspeccer',
                                     description='Plotting tool for easier poisitioning.')
    parser.add_argument('--mplrc', help='Location of a matplotlibrc to be used.',
                        default=osp.join(osp.dirname(osp.abspath(__file__)), "defaults", "matplotlibrc"))
    parser.add_argument('data', nargs='*', help='files to look at and folders to look through for fig*.py files')
    args = parser.parse_args()
    if not osp.isfile(args.mplrc):
        raise IOError(f"The 'mplrc' argument ('{args.mplrc}') has to be an existing file")
    mpl.rc_file(args.mplrc)

    if len(args.data) == 0:
        print("no data given, looking for all fig*.py files in the working directory")
        args.data = ['.']

    plotscripts = []
    for fname in args.data:
        if osp.isdir(fname):
            plotscripts.extend(glob.glob(osp.join(fname, "fig*.py")))
        elif osp.isfile(fname):
            plotscripts.append(fname)
        else:
            raise IOError(f"all data given have to be folder or files that exist, '{fname}' does not")

    mainWD = os.getcwd()
    for name in plotscripts:
        log.info(f"-- processing file {name} --")
        # always get back to main working directory
        os.chdir(mainWD)
        if osp.dirname(name) != "":
            os.chdir(osp.dirname(name))
        core.make_figure(osp.splitext(osp.basename(name))[0])


if __name__ == "__main__":
    import sys
    from inspect import isfunction, getargspec
    local_globals = list(globals().keys())

    def is_noarg_function(f):
        "Test if f is valid function and has no arguments"
        func = globals()[f]
        if isfunction(func):
            argspec = getargspec(func)
            if len(argspec.args) == 0\
                        and argspec.varargs is None\
                        and argspec.keywords is None:
                return True
        return False

    def show_functions():
        functions.sort()
        for f in functions:
            print(f)
    functions = [f for f in local_globals if is_noarg_function(f)]
    if len(sys.argv) <= 1 or sys.argv[1] == "-h":
        show_functions()
    else:
        for launch in sys.argv[1:]:
            if launch in functions:
                run = globals()[launch]
                run()
            else:
                print(launch, "not part of functions:")
                show_functions()
