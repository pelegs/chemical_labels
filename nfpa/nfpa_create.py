#!/usr/bin/env python3
# -*- coding: iso-8859-15 -*-

import argparse
from subprocess import call


parser = argparse.ArgumentParser()
parser.add_argument('-f', '--flammability', default=0, type=int)
parser.add_argument('-hea', '--health', default=0, type=int)
parser.add_argument('-ins', '--instability', default=0, type=int)
parser.add_argument('-s', '--special', default='', type=str)
args = parser.parse_args()

cmd = 'pdflatex '
cmd += '"\\def\\flam{{{}}} '.format(args.flammability)
cmd += '\\def\\health{{{}}} '.format(args.health)
cmd += '\\def\\instab{{{}}} '.format(args.instability)
cmd += '\\def\\spec{{{}}} '.format(args.special)
cmd += '\\input{nfpa_tikz}"'

call(cmd, shell=True)
