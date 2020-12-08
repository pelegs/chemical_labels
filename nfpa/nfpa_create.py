#!/usr/bin/env python3
# -*- coding: iso-8859-15 -*-

"""
Generates an NFPA pictogram as SVG
and PDF files.
"""

from sys import argv
import svgutils.transform as sg
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPDF, renderPM

material_name = argv[1]

fig = sg.fromfile('nfpa_diamond.svg')
flammability = sg.TextElement(46.7,35, text=argv[2], size=24, font='Arial', weight='normal')
health = sg.TextElement(20,61, text=argv[3], size=24, font='Arial', weight='normal')
instability = sg.TextElement(73,61, text=argv[4], size=24, font='Arial', weight='normal')

if len(argv) == 6:
    special_text = argv[5]
else:
    special_text = ''
special = sg.TextElement(45,90, text=special_text, size=24, font='Arial', weight='normal')

fig.append([flammability, health, instability, special])
fig.save('{}_diamond.svg'.format(material_name))

drawing = svg2rlg('{}_diamond.svg'.format(material_name))
renderPDF.drawToFile(drawing, '{}_diamond.pdf'.format(material_name))
