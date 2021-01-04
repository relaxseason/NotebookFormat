# -*- coding:utf-8 -*-
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
from reportlab.lib import colors
from logging import getLogger
import math
logger = getLogger(__name__)

colorsList = [
    (colors.aquamarine, "aquamarine"),
    (colors.burlywood, "burlywood"),
    (colors.darkgoldenrod, "darkgoldenrod"),
    (colors.darkgray, "darkgray"),
    (colors.darkkhaki, "darkkhaki"),
    (colors.darkorange, "darkorange"),
    (colors.darksalmon, "darksalmon"),
    (colors.darkseagreen, "darkseagreen"),
    (colors.fidlightblue, "fidlightblue"),
    (colors.gainsboro, "gainsboro"),
    (colors.gold, "gold"),
    (colors.greenyellow, "greenyellow"),
    (colors.khaki, "khaki"),
    (colors.lavender, "lavender"),
    (colors.lightblue, "lightblue"),
    (colors.lightcyan, "lightcyan"),
    (colors.lightgreen, "lightgreen"),
    (colors.lightgrey, "lightgrey"),
    (colors.lightpink, "lightpink"),
    (colors.lightsalmon, "lightsalmon"),
    (colors.lightskyblue, "lightskyblue"),
    (colors.mediumpurple, "mediumpurple"),
    (colors.mediumseagreen, "mediumseagreen"),
    (colors.mediumturquoise, "mediumturquoise"),
    (colors.olive, "olive"),
    (colors.olivedrab, "olivedrab"),
    (colors.palegreen, "palegreen"),
    (colors.paleturquoise, "paleturquoise"),
    (colors.peachpuff, "peachpuff"),
    (colors.powderblue, "powderblue"),
    (colors.silver, "silver"),
    (colors.tan, "tan"),
    (colors.thistle, "thistle"),
    (colors.wheat, "wheat"), ]
# pdfFile.setFillColorRGB(128, 128, 128)

for color, colorName in colorsList:
    outDir = "./pdf"
    outFileName = "A5-M81B"
    outFileExt = "pdf"
    path = "{0}/{1}-{2}.{3}".format(outDir, outFileName, colorName, outFileExt)
    pdfFile = canvas.Canvas(path)
    pdfFile.saveState()

    pdfFile.setAuthor('relaxseason')
    pdfFile.setTitle('A5用 M81罫B{0}'.format(colorName))
    pdfFile.setSubject('A5用 M81罫B')

    # A4
    a4width = 210
    a4height = 297
    pdfFile.setPageSize((a4width*mm, a4height*mm))

    # A5
    a5width = a4height/2
    a5height = a4width

    # ラインの色指定
    pdfFile.setStrokeColor(color)

    # ラインの太さを変更する
    pdfFile.setLineWidth(0.1*mm)

    # M9用の9マスを追加する

    # 表の描画
    xbindingSpace = 10
    ybindingSpace = xbindingSpace
    cellsize = (a5width - xbindingSpace*2)/9
    xmargin = (a5width - (cellsize * 9))/2
    ymargin = (a5height - (cellsize * 9))/2

    # 切り取り線
    top = a5height - ymargin + ybindingSpace
    bottom = ymargin - ybindingSpace
    pdfFile.line(top * mm, 0, top * mm, a4height * mm)
    pdfFile.line(bottom * mm, 0, bottom * mm, a4height * mm)
    pdfFile.line(0, a5width * mm, a4width * mm, a5width * mm)

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
        pdfFile.grid(ylist, xlist)

        # 2ページ目
        pdfFile.grid(ylist, [x+a5width*mm for x in xlist])

        pdfFile.setLineWidth(1)
        pdfFile.rect((y+cellsize)*mm, (x+cellsize)*mm,
                     cellsize*mm, cellsize*mm)
        # 2ページ目
        pdfFile.rect((y+cellsize)*mm, (x+cellsize+a5width)*mm,
                     cellsize*mm, cellsize*mm)

    # 外側の箱の区切り線
    pdfFile.setLineWidth(1)
    for i in [i*3*cellsize for i in [1, 2]]:
        pdfFile.line(ymargin * mm, (xmargin + i) * mm,
                     (ymargin + cellsize * 9) * mm, (xmargin + i) * mm)
        pdfFile.line((ymargin + i) * mm, xmargin * mm,
                     (ymargin + i) * mm, (xmargin + cellsize * 9) * mm)

    # 2ページ目
    for i in [i*3*cellsize for i in [1, 2]]:
        pdfFile.line(ymargin * mm, (xmargin + i+a5width) * mm,
                     (ymargin + cellsize * 9) * mm, (xmargin + i+a5width) * mm)
        pdfFile.line((ymargin + i) * mm, (xmargin+a5width) * mm,
                     (ymargin + i) * mm, (xmargin + cellsize * 9+a5width) * mm)

    # 中央の曼陀羅
    # ラインの太さを変更する
    pdfFile.setLineWidth(1)
    x_space = xmargin
    y_space = ymargin
    xlist = [(x_space + cellsize * (i+3)) * mm for i in range(4)]
    ylist = [(y_space + cellsize * (i+3)) * mm for i in range(4)]
    pdfFile.grid(ylist, xlist)
    pdfFile.grid(ylist, [x+a5width*mm for x in xlist])  # 2ページ目

    # 余白のドット方眼
    pdfFile.setFillColor(color)
    # 第1
    dotspace1st = 1.25
    for x, y in [((x)*dotspace1st, (y)*dotspace1st)
                 for x in range(math.ceil(a4height/dotspace1st))
                 for y in range(math.ceil((ymargin-ybindingSpace)/dotspace1st))]:
        pdfFile.circle(y*mm, x*mm, 0.15*mm, stroke=0, fill=1)
        pdfFile.circle((top+y)*mm, x*mm, 0.15*mm, stroke=0, fill=1)

    # 第2
    dotspace2nd = 5
    for x, y in [((x)*dotspace2nd, (y)*dotspace2nd)
                 for x in range(math.ceil(a4height/dotspace2nd))
                 for y in range(math.ceil((ymargin-ybindingSpace)/dotspace2nd))]:
        pdfFile.circle(y*mm, x*mm, 0.25*mm, stroke=0, fill=1)
        pdfFile.circle((top+y)*mm, x*mm, 0.25*mm, stroke=0, fill=1)

    pdfFile.restoreState()
    pdfFile.save()
