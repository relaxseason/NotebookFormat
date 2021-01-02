# -*- coding:utf-8 -*-
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
from reportlab.lib import colors
from logging import getLogger
import math
logger = getLogger(__name__)

# 出力先設定
outPath = "./pdf"
outFileName = "FLEXD3-Dot"
outFileExt = "pdf"
pdfFile = canvas.Canvas("{0}/{1}.{2}".format(outPath, outFileName, outFileExt))
pdfFile.saveState()

# Property
pdfFile.setAuthor('relaxseason')
pdfFile.setTitle('FLEXNOTE D3用 ドット')
pdfFile.setSubject('FLEXNOTE D3用 ドット')

# A4
a4width = 210
a4height = 297
a4width_mm = a4width*mm
a4height_mm = a4height*mm
pdfFile.setPageSize((a4width_mm, a4height_mm))

# ラインの色指定
linecolor = colors.blue
# linecolor = colors.green
pdfFile.setStrokeColor(linecolor)
# pdfFile.setFillColorRGB(128, 128, 128)

# ラインの太さを変更する
pdfFile.setLineWidth(0.1*mm)

# A5サイズにラインを入れる
half_height = 148.5
half_height_mm = half_height * mm
pdfFile.line(0, half_height_mm, a4width*mm, half_height_mm)

# D3サイズにラインを入れる
d3width = 90
d3width1_mm = d3width * mm
d3width2_mm = d3width * 2 * mm
pdfFile.line(d3width1_mm, 0, d3width1_mm, a4height_mm)
pdfFile.line(d3width2_mm, 0, d3width2_mm, a4height_mm)

# ドット方眼
pdfFile.setFillColor(linecolor)
dotspace1st = 1.25
for x, y in [((x)*dotspace1st, (y)*dotspace1st)
             for x in range(math.ceil(a4width/dotspace1st))
             for y in range(math.ceil(a4height/dotspace1st))]:
    pdfFile.circle(x*mm, y*mm, 0.15*mm, stroke=0, fill=1)

dotspace2nd = 5
for x, y in [((x)*dotspace2nd, (y)*dotspace2nd)
             for x in range(math.ceil(a4width/dotspace2nd))
             for y in range(math.ceil(a4height/dotspace2nd))]:
    pdfFile.circle(x*mm, y*mm, 0.25*mm, stroke=0, fill=1)


pdfFile.restoreState()
pdfFile.save()
