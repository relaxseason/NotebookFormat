# -*- coding:utf-8 -*-
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
from reportlab.lib import colors
from logging import getLogger
import math
import os
logger = getLogger(__name__)


outDir = "./pdf/M9"
if not os.path.exists(outDir):
    os.makedirs(outDir, exist_ok=True)

outFileName = "A4-M81B"
outFileExt = "pdf"
pdfFile = canvas.Canvas("{0}/{1}.{2}".format(outDir, outFileName, outFileExt))
pdfFile.saveState()

pdfFile.setAuthor('relaxseason')
pdfFile.setTitle('A4用 M81罫B')
pdfFile.setSubject('A4用 M81罫B')

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

# M9用の9マスを追加する


# 表の描画
xbindingSpace = 11
ybindingSpace = xbindingSpace-1
cellsize = (a4width - xbindingSpace*2)/9
xmargin = (a4width - (cellsize * 9))/2
ymargin = (a4height - (cellsize * 9))/2

# 切り取り線
top = a4height - ymargin + ybindingSpace
bottom = ymargin - ybindingSpace
pdfFile.line(0, top * mm, a4width * mm, top * mm)
pdfFile.line(0, bottom * mm, a4width * mm, bottom * mm)

# 8個の曼陀羅
outBox = [(x, y)
          for x in range(3)
          for y in range(3)
          if(not(x == 1 & y == 1))]

for x, y in [(xmargin + cellsize * x * 3,
              ymargin + cellsize * y * 3)
             for x, y in outBox]:
    xlist = [(x + cellsize * i) * mm for i in [0, 1, 2, 3]]
    ylist = [(y + cellsize * i) * mm for i in [0, 1, 2, 3]]

    pdfFile.setLineWidth(0.1*mm)
    pdfFile.grid(xlist, ylist)

    pdfFile.setLineWidth(1)
    pdfFile.rect((x+cellsize)*mm, (y+cellsize)*mm,
                 cellsize*mm, cellsize*mm)

# 外側の箱の区切り線
pdfFile.setLineWidth(1)
for i in [i*3*cellsize for i in [1, 2]]:
    pdfFile.line((xmargin + i) * mm, ymargin * mm,
                 (xmargin + i) * mm, (ymargin + cellsize * 9) * mm)
    pdfFile.line(xmargin * mm, (ymargin + i) * mm,
                 (xmargin + cellsize * 9) * mm, (ymargin + i) * mm)

# 中央の曼陀羅
# ラインの太さを変更する
pdfFile.setLineWidth(1)
x_space = xmargin
y_space = ymargin
xlist = [(x_space + cellsize * (i+3)) * mm for i in range(4)]
ylist = [(y_space + cellsize * (i+3)) * mm for i in range(4)]
pdfFile.grid(xlist, ylist)

# 余白のドット方眼
pdfFile.setFillColor(linecolor)
dotspace1st = 1.25
for x, y in [((x)*dotspace1st, (y)*dotspace1st)
             for x in range(math.ceil(a4width/dotspace1st))
             for y in range(math.ceil((ymargin-ybindingSpace)/dotspace1st))]:
    pdfFile.circle(x*mm, y*mm, 0.15*mm, stroke=0, fill=1)
    pdfFile.circle(x*mm, (top+y)*mm, 0.15*mm, stroke=0, fill=1)

dotspace2nd = 5
for x, y in [((x)*dotspace2nd, (y)*dotspace2nd)
             for x in range(math.ceil(a4width/dotspace2nd))
             for y in range(math.ceil((ymargin-ybindingSpace)/dotspace2nd))]:
    pdfFile.circle(x*mm, y*mm, 0.25*mm, stroke=0, fill=1)
    pdfFile.circle(x*mm, (top+y)*mm, 0.25*mm, stroke=0, fill=1)


pdfFile.restoreState()
pdfFile.save()
