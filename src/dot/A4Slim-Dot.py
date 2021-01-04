# -*- coding:utf-8 -*-
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
from reportlab.lib import colors
from logging import getLogger
import math
logger = getLogger(__name__)

# 出力先設定
outPath = "./pdf"
outFileName = "A4Slim-Dot"
outFileExt = "pdf"
pdfFile = canvas.Canvas("{0}/{1}.{2}".format(outPath, outFileName, outFileExt))
pdfFile.saveState()

pdfFile.setAuthor('relaxseason')
pdfFile.setTitle('A4 Slim 1.25ドット方眼')
pdfFile.setSubject('A4 Slim 1.25ドット方眼')

# A4
a4width = 210
a4height = 297
a4width_mm = a4width*mm
a4height_mm = a4height*mm
pdfFile.setPageSize((a4width*mm, a4height*mm))
# B5
# pdfFile.setPageSize((18.2*cm, 25.7*cm))

# ラインの色指定
# linecolor = colors.blue
# linecolor = colors.orange
linecolor = colors.lightsalmon
# linecolor = colors.green
pdfFile.setStrokeColor(linecolor)
# pdfFile.setFillColorRGB(128, 128, 128)

# ラインの太さを変更する
pdfFile.setLineWidth(0.01*mm)

# A5 slimサイズ(210x99)にラインを入れる
half_height = a4height/3
pdfFile.line(0, half_height*mm, a4width*mm, half_height*mm)
pdfFile.line(0, half_height*2*mm, a4width*mm, half_height*2*mm)

# ドット方眼
pdfFile.setFillColor(linecolor)
dotspace1st = 1.25
for x, y in [((x)*dotspace1st, (y)*dotspace1st)
             for x in range(math.ceil(a4width/dotspace1st)+1)
             for y in range(math.ceil(a4height/dotspace1st)+1)]:
    pdfFile.circle(x*mm, y*mm, 0.15*mm, stroke=0, fill=1)

dotspace2nd = 5
for x, y in [((x)*dotspace2nd, (y)*dotspace2nd)
             for x in range(math.ceil(a4width/dotspace2nd)+1)
             for y in range(math.ceil(a4height/dotspace2nd)+1)]:
    pdfFile.circle(x*mm, y*mm, 0.25*mm, stroke=0, fill=1)


pdfFile.restoreState()
pdfFile.save()
