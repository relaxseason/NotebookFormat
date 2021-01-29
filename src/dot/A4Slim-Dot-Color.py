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
    # 出力先設定
    outPath = "./pdf/A5Slim-Dot-Color2"
    outFileName = "A4Slim-Dot"
    outFileExt = "pdf"
    path = "{0}/{1}-{2}.{3}".format(outPath,
                                    outFileName, colorName, outFileExt)
    pdfFile = canvas.Canvas(path)
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

    # ラインの色指定
    linecolor = color
    # linecolor = colors.green
    pdfFile.setStrokeColor(linecolor)
    # pdfFile.setFillColorRGB(128, 128, 128)

    # ラインの太さを変更する
    pdfFile.setLineWidth(0.01*mm)

    # A5 slimサイズ(210x99)にラインを入れる
    half_height = a4height/3
    pdfFile.line(0, a4height*mm, a4width*mm, a4height*mm)
    pdfFile.line(0, half_height*mm, a4width*mm, half_height*mm)
    pdfFile.line(0, half_height*2*mm, a4width*mm, half_height*2*mm)
    pdfFile.line(0, 0, a4width*mm, 0)

    # ドット方眼
    pdfFile.setFillColor(linecolor)
    dotspace1st = 1.25
    for x, y in [((x)*dotspace1st, (y)*dotspace1st)
                 for x in range(math.ceil(a4width/dotspace1st)+1)
                 for y in range(math.ceil(a4height/dotspace1st)+1)]:
        pdfFile.circle(x*mm, y*mm, 0.1*mm, stroke=0, fill=1)

    dotspace2nd = 5
    for x, y in [((x)*dotspace2nd, (y)*dotspace2nd)
                 for x in range(math.ceil(a4width/dotspace2nd)+1)
                 for y in range(math.ceil(a4height/dotspace2nd)+1)]:
        pdfFile.circle(x*mm, y*mm, 0.2*mm, stroke=0, fill=1)

    pdfFile.restoreState()
    pdfFile.save()
