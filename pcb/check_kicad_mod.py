#!/usr/bin/env python

from __future__ import print_function

import argparse
from kicad_mod import *
from print_color import *
import checkrule6_3, checkrule6_4, checkrule6_5, checkrule6_6, checkrule6_9
import checkrule10_1, checkrule10_2, checkrule10_3, checkrule10_4, checkrule10_5, checkrule10_6, checkrule10_7

parser = argparse.ArgumentParser()
parser.add_argument('kicad_mod_files', nargs='+')
parser.add_argument('--fix', help='fix the violations if possible', action='store_true')
parser.add_argument('--nocolor', help='does not use colors to show the output', action='store_true')
parser.add_argument('-v', '--verbose', help='show status of all modules and extra information about the violation', action='store_true')
args = parser.parse_args()

printer = PrintColor(use_color = not args.nocolor)

for filename in args.kicad_mod_files:
    module = KicadMod(filename)

    check6_3 = checkrule6_3.check_rule(module)
    check6_4 = checkrule6_4.check_rule(module)
    check6_5 = checkrule6_5.check_rule(module)
    check6_6 = checkrule6_6.check_rule(module)
    check6_9 = checkrule6_9.check_rule(module)
    check10_1 = checkrule10_1.check_rule(module)
    check10_2 = checkrule10_2.check_rule(module)
    check10_3 = checkrule10_3.check_rule(module)
    check10_4 = checkrule10_4.check_rule(module)
    check10_5 = checkrule10_5.check_rule(module)
    check10_6 = checkrule10_6.check_rule(module)
    check10_7 = checkrule10_7.check_rule(module)

    # print the violations
    if (check6_3 or check6_4 or check6_5 or check6_6 or check6_9 or
        check10_1 or check10_2 or check10_3 or check10_4 or check10_5 or check10_6 or check10_7):
        printer.green('module: %s' % module.name)

        if check6_3:
            printer.yellow('\tRule 6.3 violated')
            if args.verbose:
                printer.light_blue('\tFor through-hole components, footprint anchor is set on pad 1.')

        if check6_4:
            printer.yellow('\tRule 6.4 violated')
            if args.verbose:
                printer.light_blue('\tFor surface-mount devices, footprint anchor is placed in the middle with respect to device lead ends. (IPC-7351)')

        if check6_5:
            printer.yellow('\tRule 6.5 violated')
            if args.verbose:
                printer.light_blue('\tSilkscreen is not superposed to pads, its outline is completely visible after board assembly,')
                printer.light_blue('\tuses 0.15mm line width and provides a reference mark for pin 1. (IPC-7351)')

        if check6_6:
            printer.yellow('\tRule 6.6 violated')
            if args.verbose:
                printer.light_blue('\tCourtyard line has a width 0.05mm. This line is placed so that its clearance is measured from')
                printer.light_blue('\tits center to the edges of pads and body, and its position is rounded on a grid of 0.05mm.')

        if check6_9:
            printer.yellow('\tRule 6.9 violated')
            if args.verbose:
                printer.light_blue('\tValue and reference have a height of 1mm.')

        if check10_1:
            printer.yellow('\tRule 10.1 violated')
            if args.verbose:
                printer.light_blue('\tFootprint name must match its filename. (.kicad_mod files).')

        if check10_2:
            printer.yellow('\tRule 10.2 violated')
            if args.verbose:
                printer.light_blue('\tDoc property contains a full description of footprint.')

        if check10_3:
            printer.yellow('\tRule 10.3 violated')
            if args.verbose:
                printer.light_blue('\tKeywords are separated by spaces.')

        if check10_4:
            printer.yellow('\tRule 10.4 violated')
            if args.verbose:
                printer.light_blue('\tValue is filled with footprint name and is placed on the fabrication layer.')

        if check10_5:
            printer.yellow('\tRule 10.5 violated')
            if args.verbose:
                printer.light_blue('\tAttributes is set to the appropriate value, see tooltip for more information.')

        if check10_6:
            printer.yellow('\tRule 10.6 violated')
            if args.verbose:
                printer.light_blue('\tAll other properties are left to default values.')
                printer.light_blue('\t(Move and Place: Free; Auto Place: 0 and 0,  Local Clearance Values: 0)')

        if check10_7:
            printer.yellow('\tRule 10.7 violated')
            if args.verbose:
                printer.light_blue('\t3D Shape ".wrl" files are named the same as their footprint and are placed in a folder')
                printer.light_blue('\tnamed the same as the footprint library replacing the ".pretty" with ".3dshapes"')
