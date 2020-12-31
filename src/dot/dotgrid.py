# -*- coding:utf-8 -*-
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
from reportlab.lib import colors
from logging import getLogger
logger = getLogger(__name__)

outPath = "./pdf"
outFileName = "DotGrid"
outFileExt = "pdf"
pdfFile = canvas.Canvas("{0}/{1}.{2}".format(outPath, outFileName, outFileExt))
pdfFile.saveState()

pdfFile.setAuthor('relaxseason')
pdfFile.setTitle('ドット方眼')
pdfFile.setSubject('ドット方眼A4, 5mm')

# A4
a4width = 210
a4height = 297
pdfFile.setPageSize((a4width*mm, a4height*mm))

# pdfFile.setFillColorRGB(128, 128, 128)
pdfFile.setFillColor(colors.lightgrey)
# pdfFile.setFillColorRGB(255, 0, 0)

# 余白
x_space = 0
y_space = 0

a4width_int = a4width - x_space
a4height_int = a4height - y_space

x_count = ((a4width_int // 5))
y_count = ((a4height_int // 5))
# x_space = (a4width - x_count*5 ) #/ 2
# y_space = (a4height - y_count*5 ) #/ 2
points = [[i*5+x_space, j*5+y_space]
          for i in range(x_count) for j in range(y_count)]
# logger.debug("x_count:%i, y_count:%i, x_space:%i, y_space:%i"
# % [x_count,y_count,x_space,y_space])
for x, y in points:
    pdfFile.circle(x/1 * mm, y/1 * mm, 0.25 * mm, stroke=0, fill=1)

pdfFile.restoreState()
pdfFile.save()
