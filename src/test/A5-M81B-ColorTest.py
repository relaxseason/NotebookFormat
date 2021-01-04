# -*- coding:utf-8 -*-
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
from reportlab.lib import colors
from logging import getLogger
import math
logger = getLogger(__name__)


colorlist = [
    [(colors.aliceblue, "aliceblue"), (colors.antiquewhite, "antiquewhite")],
    [(colors.aqua, "aqua"), (colors.aquamarine, "aquamarine")],
    [(colors.azure, "azure"), (colors.beige, "beige")],
    [(colors.bisque, "bisque"), (colors.black, "black")],
    [(colors.blanchedalmond, "blanchedalmond"), (colors.blue, "blue")],
    [(colors.blueviolet, "blueviolet"), (colors.brown, "brown")],
    [(colors.burlywood, "burlywood"), (colors.cadetblue, "cadetblue")],
    [(colors.chartreuse, "chartreuse"), (colors.chocolate, "chocolate")],
    [(colors.coral, "coral"), (colors.cornflowerblue, "cornflowerblue")],
    [(colors.cornsilk, "cornsilk"), (colors.crimson, "crimson")],
    [(colors.cyan, "cyan"), (colors.darkblue, "darkblue")],
    [(colors.darkcyan, "darkcyan"), (colors.darkgoldenrod, "darkgoldenrod")],
    [(colors.darkgray, "darkgray"), (colors.darkgrey, "darkgrey")],
    [(colors.darkgreen, "darkgreen"), (colors.darkkhaki, "darkkhaki")],
    [(colors.darkmagenta, "darkmagenta"),
     (colors.darkolivegreen, "darkolivegreen")],
    [(colors.darkorange, "darkorange"), (colors.darkorchid, "darkorchid")],
    [(colors.darkred, "darkred"), (colors.darksalmon, "darksalmon")],
    [(colors.darkseagreen, "darkseagreen"),
     (colors.darkslateblue, "darkslateblue")],
    [(colors.darkslategray, "darkslategray"),
     (colors.darkslategrey, "darkslategrey")],
    [(colors.darkturquoise, "darkturquoise"), (colors.darkviolet, "darkviolet")],
    [(colors.deeppink, "deeppink"), (colors.deepskyblue, "deepskyblue")],
    [(colors.dimgray, "dimgray"), (colors.dimgrey, "dimgrey")],
    [(colors.dodgerblue, "dodgerblue"), (colors.firebrick, "firebrick")],
    [(colors.floralwhite, "floralwhite"), (colors.forestgreen, "forestgreen")],
    [(colors.fuchsia, "fuchsia"), (colors.gainsboro, "gainsboro")],
    [(colors.ghostwhite, "ghostwhite"), (colors.gold, "gold")],
    [(colors.goldenrod, "goldenrod"), (colors.gray, "gray")],
    [(colors.grey, "grey"), (colors.green, "green")],
    [(colors.greenyellow, "greenyellow"), (colors.honeydew, "honeydew")],
    [(colors.hotpink, "hotpink"), (colors.indianred, "indianred")],
    [(colors.indigo, "indigo"), (colors.ivory, "ivory")],
    [(colors.khaki, "khaki"), (colors.lavender, "lavender")],
    [(colors.lavenderblush, "lavenderblush"), (colors.lawngreen, "lawngreen")],
    [(colors.lemonchiffon, "lemonchiffon"), (colors.lightblue, "lightblue")],
    [(colors.lightcoral, "lightcoral"), (colors.lightcyan, "lightcyan")],
    [(colors.lightgoldenrodyellow, "lightgoldenrodyellow"),
     (colors.lightgreen, "lightgreen")],
    [(colors.lightgrey, "lightgrey"), (colors.lightpink, "lightpink")],
    [(colors.lightsalmon, "lightsalmon"),
     (colors.lightseagreen, "lightseagreen")],
    [(colors.lightskyblue, "lightskyblue"),
     (colors.lightslategray, "lightslategray")],
    [(colors.lightslategrey, "lightslategrey"),
     (colors.lightsteelblue, "lightsteelblue")],
    [(colors.lightyellow, "lightyellow"), (colors.lime, "lime")],
    [(colors.limegreen, "limegreen"), (colors.linen, "linen")],
    [(colors.magenta, "magenta"), (colors.maroon, "maroon")],
    [(colors.mediumaquamarine, "mediumaquamarine"),
     (colors.mediumblue, "mediumblue")],
    [(colors.mediumorchid, "mediumorchid"),
     (colors.mediumpurple, "mediumpurple")],
    [(colors.mediumseagreen, "mediumseagreen"),
     (colors.mediumslateblue, "mediumslateblue")],
    [(colors.mediumspringgreen, "mediumspringgreen"),
     (colors.mediumturquoise, "mediumturquoise")],
    [(colors.mediumvioletred, "mediumvioletred"),
     (colors.midnightblue, "midnightblue")],
    [(colors.mintcream, "mintcream"), (colors.mistyrose, "mistyrose")],
    [(colors.moccasin, "moccasin"), (colors.navajowhite, "navajowhite")],
    [(colors.navy, "navy"), (colors.oldlace, "oldlace")],
    [(colors.olive, "olive"), (colors.olivedrab, "olivedrab")],
    [(colors.orange, "orange"), (colors.orangered, "orangered")],
    [(colors.orchid, "orchid"), (colors.palegoldenrod, "palegoldenrod")],
    [(colors.palegreen, "palegreen"), (colors.paleturquoise, "paleturquoise")],
    [(colors.palevioletred, "palevioletred"),
     (colors.papayawhip, "papayawhip")],
    [(colors.peachpuff, "peachpuff"), (colors.peru, "peru")],
    [(colors.pink, "pink"), (colors.plum, "plum")],
    [(colors.powderblue, "powderblue"), (colors.purple, "purple")],
    [(colors.red, "red"), (colors.rosybrown, "rosybrown")],
    [(colors.royalblue, "royalblue"), (colors.saddlebrown, "saddlebrown")],
    [(colors.salmon, "salmon"), (colors.sandybrown, "sandybrown")],
    [(colors.seagreen, "seagreen"), (colors.seashell, "seashell")],
    [(colors.sienna, "sienna"), (colors.silver, "silver")],
    [(colors.skyblue, "skyblue"), (colors.slateblue, "slateblue")],
    [(colors.slategray, "slategray"), (colors.slategrey, "slategrey")],
    [(colors.snow, "snow"), (colors.springgreen, "springgreen")],
    [(colors.steelblue, "steelblue"), (colors.tan, "tan")],
    [(colors.teal, "teal"), (colors.thistle, "thistle")],
    [(colors.tomato, "tomato"), (colors.turquoise, "turquoise")],
    [(colors.violet, "violet"), (colors.wheat, "wheat")],
    [(colors.white, "white"), (colors.whitesmoke, "whitesmoke")],
    [(colors.yellow, "yellow"), (colors.yellowgreen, "yellowgreen")],
    [(colors.fidblue, "fidblue"), (colors.fidred, "fidred")],
    [(colors.fidlightblue, "fidlightblue"),
     (colors.fidlightblue, "fidlightblue")]
]

for color1, color2 in colorlist:
    outDir = "./pdftest2"
    outFileName = "A5-M81B"
    outFileExt = "pdf"
    linecolor1 = color1[0]
    colorStr1 = color1[1]
    linecolor2 = color2[0]
    colorStr2 = color2[1]
    path = "{0}/{1}-{2}-{3}.{4}".format(outDir, outFileName,
                                        colorStr1, colorStr2, outFileExt)
    pdfFile = canvas.Canvas(path)
    pdfFile.saveState()

    pdfFile.setAuthor('relaxseason')
    pdfFile.setTitle('A5用 M81罫B')
    pdfFile.setSubject('A5用 M81罫B')

    # A4
    a4width = 210
    a4height = 297
    pdfFile.setPageSize((a4width*mm, a4height*mm))

    # A5
    a5width = a4height/2
    a5height = a4width

    # ラインの色指定
    pdfFile.setStrokeColor(linecolor1)
    # pdfFile.setStrokeColor(linecolor2)

    # ラインの太さを変更する
    pdfFile.setLineWidth(0.1*mm)

    # M9用の9マスを追加する
    # 表の描画位置
    xbindingSpace = 10
    ybindingSpace = xbindingSpace
    cellsize = (a5width - xbindingSpace*2)/9
    xmargin = (a5width - (cellsize * 9))/2
    ymargin = (a5height - (cellsize * 9))/2

    # 色名を追加
    # フォント関連設定
    pdfFile.setFont("Times-Roman", 8)
    pdfFile.setFillColor(colors.black)

    # 1ページ目
    leftNameX = ymargin + cellsize * 7 - 2
    leftNameY = a5width - 5
    pdfFile.drawString(leftNameX * mm, leftNameY * mm, colorStr1)
    # 2ページ目
    rightNameX = ymargin + cellsize * 7 - 2
    rightNameY = a4height - 5
    pdfFile.drawString(rightNameX * mm, rightNameY * mm, colorStr2)

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
        pdfFile.setStrokeColor(linecolor1)
        pdfFile.grid(ylist, xlist)

        # 2ページ目
        pdfFile.setStrokeColor(linecolor2)
        pdfFile.grid(ylist, [x+a5width*mm for x in xlist])

        pdfFile.setLineWidth(1)
        pdfFile.setStrokeColor(linecolor1)
        pdfFile.rect((y+cellsize)*mm, (x+cellsize)*mm,
                     cellsize*mm, cellsize*mm)
        # 2ページ目
        pdfFile.setStrokeColor(linecolor2)
        pdfFile.rect((y+cellsize)*mm, (x+cellsize+a5width)*mm,
                     cellsize*mm, cellsize*mm)

    # 外側の箱の区切り線
    pdfFile.setLineWidth(1)
    pdfFile.setStrokeColor(linecolor1)
    for i in [i*3*cellsize for i in [1, 2]]:
        pdfFile.line(ymargin * mm, (xmargin + i) * mm,
                     (ymargin + cellsize * 9) * mm, (xmargin + i) * mm)
        pdfFile.line((ymargin + i) * mm, xmargin * mm,
                     (ymargin + i) * mm, (xmargin + cellsize * 9) * mm)

    # 2ページ目
    pdfFile.setStrokeColor(linecolor2)
    for i in [i*3*cellsize for i in [1, 2]]:
        pdfFile.line(ymargin * mm, (xmargin + i+a5width) * mm,
                     (ymargin + cellsize * 9) * mm, (xmargin + i+a5width) * mm)
        pdfFile.line((ymargin + i) * mm, (xmargin+a5width) * mm,
                     (ymargin + i) * mm, (xmargin + cellsize * 9+a5width) * mm)

    # 中央の曼陀羅
    # ラインの太さを変更する
    pdfFile.setStrokeColor(linecolor1)
    pdfFile.setLineWidth(1)
    x_space = xmargin
    y_space = ymargin
    xlist = [(x_space + cellsize * (i+3)) * mm for i in range(4)]
    ylist = [(y_space + cellsize * (i+3)) * mm for i in range(4)]
    pdfFile.grid(ylist, xlist)
    pdfFile.setStrokeColor(linecolor2)
    pdfFile.grid(ylist, [x+a5width*mm for x in xlist])  # 2ページ目

    # 余白のドット方眼
    pdfFile.setFillColor(linecolor1)
    # 第1
    # 1ページ目
    dotspace1st = 1.25
    for x, y in [((x)*dotspace1st, (y)*dotspace1st)
                 for x in range(math.ceil(a5width/dotspace1st))
                 for y in range(math.ceil((ymargin-ybindingSpace)
                                          / dotspace1st))]:
        pdfFile.circle(y*mm, x*mm, 0.15*mm, stroke=0, fill=1)
        pdfFile.circle((top+y)*mm, x*mm, 0.15*mm, stroke=0, fill=1)
    # 2ページ目
    pdfFile.setFillColor(linecolor2)
    for x, y in [(x*dotspace1st+a5width, (y)*dotspace1st)
                 for x in range(math.ceil(a5width/dotspace1st))
                 for y in range(math.ceil((ymargin-ybindingSpace)
                                          / dotspace1st))]:
        pdfFile.circle(y*mm, x*mm, 0.15*mm, stroke=0, fill=1)
        pdfFile.circle((top+y)*mm, x*mm, 0.15*mm, stroke=0, fill=1)

    # 第2
    # 1ページ目
    pdfFile.setFillColor(linecolor1)
    dotspace2nd = 5
    for x, y in [((x)*dotspace2nd, (y)*dotspace2nd)
                 for x in range(math.ceil(a5width/dotspace2nd))
                 for y in range(math.ceil((ymargin-ybindingSpace)
                                          / dotspace2nd))]:
        pdfFile.circle(y*mm, x*mm, 0.25*mm, stroke=0, fill=1)
        pdfFile.circle((top+y)*mm, x*mm, 0.25*mm, stroke=0, fill=1)
    # 2ページ目
    pdfFile.setFillColor(linecolor2)
    for x, y in [(x*dotspace2nd+a5width, (y)*dotspace2nd)
                 for x in range(math.ceil(a5width/dotspace2nd))
                 for y in range(math.ceil((ymargin-ybindingSpace)
                                          / dotspace2nd))]:
        pdfFile.circle(y*mm, x*mm, 0.25*mm, stroke=0, fill=1)
        pdfFile.circle((top+y)*mm, x*mm, 0.25*mm, stroke=0, fill=1)

    pdfFile.restoreState()
    pdfFile.save()
