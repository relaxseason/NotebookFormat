# -*- coding:utf-8 -*-
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
from reportlab.lib import colors
from logging import getLogger
import math
logger = getLogger(__name__)


colorlist = [
    (colors.aliceblue, "aliceblue"),
    (colors.antiquewhite, "antiquewhite"),
    (colors.aqua, "aqua"),
    (colors.aquamarine, "aquamarine"),
    (colors.azure, "azure"),
    (colors.beige, "beige"),
    (colors.bisque, "bisque"),
    (colors.black, "black"),
    (colors.blanchedalmond, "blanchedalmond"),
    (colors.blue, "blue"),
    (colors.blueviolet, "blueviolet"),
    (colors.brown, "brown"),
    (colors.burlywood, "burlywood"),
    (colors.cadetblue, "cadetblue"),
    (colors.chartreuse, "chartreuse"),
    (colors.chocolate, "chocolate"),
    (colors.coral, "coral"),
    (colors.cornflowerblue, "cornflowerblue"),
    (colors.cornsilk, "cornsilk"),
    (colors.crimson, "crimson"),
    (colors.cyan, "cyan"),
    (colors.darkblue, "darkblue"),
    (colors.darkcyan, "darkcyan"),
    (colors.darkgoldenrod, "darkgoldenrod"),
    (colors.darkgray, "darkgray"),
    (colors.darkgreen, "darkgreen"),
    (colors.darkgrey, "darkgrey"),
    (colors.darkkhaki, "darkkhaki"),
    (colors.darkmagenta, "darkmagenta"),
    (colors.darkolivegreen, "darkolivegreen"),
    (colors.darkorange, "darkorange"),
    (colors.darkorchid, "darkorchid"),
    (colors.darkred, "darkred"),
    (colors.darksalmon, "darksalmon"),
    (colors.darkseagreen, "darkseagreen"),
    (colors.darkslateblue, "darkslateblue"),
    (colors.darkslategray, "darkslategray"),
    (colors.darkslategrey, "darkslategrey"),
    (colors.darkturquoise, "darkturquoise"),
    (colors.darkviolet, "darkviolet"),
    (colors.deeppink, "deeppink"),
    (colors.deepskyblue, "deepskyblue"),
    (colors.dimgray, "dimgray"),
    (colors.dimgrey, "dimgrey"),
    (colors.dodgerblue, "dodgerblue"),
    (colors.fidblue, "fidblue"),
    (colors.fidlightblue, "fidlightblue"),
    (colors.fidred, "fidred"),
    (colors.firebrick, "firebrick"),
    (colors.floralwhite, "floralwhite"),
    (colors.forestgreen, "forestgreen"),
    (colors.fuchsia, "fuchsia"),
    (colors.gainsboro, "gainsboro"),
    (colors.ghostwhite, "ghostwhite"),
    (colors.gold, "gold"),
    (colors.goldenrod, "goldenrod"),
    (colors.gray, "gray"),
    (colors.green, "green"),
    (colors.greenyellow, "greenyellow"),
    (colors.grey, "grey"),
    (colors.honeydew, "honeydew"),
    (colors.hotpink, "hotpink"),
    (colors.indianred, "indianred"),
    (colors.indigo, "indigo"),
    (colors.ivory, "ivory"),
    (colors.khaki, "khaki"),
    (colors.lavender, "lavender"),
    (colors.lavenderblush, "lavenderblush"),
    (colors.lawngreen, "lawngreen"),
    (colors.lemonchiffon, "lemonchiffon"),
    (colors.lightblue, "lightblue"),
    (colors.lightcoral, "lightcoral"),
    (colors.lightcyan, "lightcyan"),
    (colors.lightgoldenrodyellow, "lightgoldenrodyellow"),
    (colors.lightgreen, "lightgreen"),
    (colors.lightgrey, "lightgrey"),
    (colors.lightpink, "lightpink"),
    (colors.lightsalmon, "lightsalmon"),
    (colors.lightseagreen, "lightseagreen"),
    (colors.lightskyblue, "lightskyblue"),
    (colors.lightslategray, "lightslategray"),
    (colors.lightslategrey, "lightslategrey"),
    (colors.lightsteelblue, "lightsteelblue"),
    (colors.lightyellow, "lightyellow"),
    (colors.lime, "lime"),
    (colors.limegreen, "limegreen"),
    (colors.linen, "linen"),
    (colors.magenta, "magenta"),
    (colors.maroon, "maroon"),
    (colors.mediumaquamarine, "mediumaquamarine"),
    (colors.mediumblue, "mediumblue"),
    (colors.mediumorchid, "mediumorchid"),
    (colors.mediumpurple, "mediumpurple"),
    (colors.mediumseagreen, "mediumseagreen"),
    (colors.mediumslateblue, "mediumslateblue"),
    (colors.mediumspringgreen, "mediumspringgreen"),
    (colors.mediumturquoise, "mediumturquoise"),
    (colors.mediumvioletred, "mediumvioletred"),
    (colors.midnightblue, "midnightblue"),
    (colors.mintcream, "mintcream"),
    (colors.mistyrose, "mistyrose"),
    (colors.moccasin, "moccasin"),
    (colors.navajowhite, "navajowhite"),
    (colors.navy, "navy"),
    (colors.oldlace, "oldlace"),
    (colors.olive, "olive"),
    (colors.olivedrab, "olivedrab"),
    (colors.orange, "orange"),
    (colors.orangered, "orangered"),
    (colors.orchid, "orchid"),
    (colors.palegoldenrod, "palegoldenrod"),
    (colors.palegreen, "palegreen"),
    (colors.paleturquoise, "paleturquoise"),
    (colors.palevioletred, "palevioletred"),
    (colors.papayawhip, "papayawhip"),
    (colors.peachpuff, "peachpuff"),
    (colors.peru, "peru"),
    (colors.pink, "pink"),
    (colors.plum, "plum"),
    (colors.powderblue, "powderblue"),
    (colors.purple, "purple"),
    (colors.red, "red"),
    (colors.rosybrown, "rosybrown"),
    (colors.royalblue, "royalblue"),
    (colors.saddlebrown, "saddlebrown"),
    (colors.salmon, "salmon"),
    (colors.sandybrown, "sandybrown"),
    (colors.seagreen, "seagreen"),
    (colors.seashell, "seashell"),
    (colors.sienna, "sienna"),
    (colors.silver, "silver"),
    (colors.skyblue, "skyblue"),
    (colors.slateblue, "slateblue"),
    (colors.slategray, "slategray"),
    (colors.slategrey, "slategrey"),
    (colors.snow, "snow"),
    (colors.springgreen, "springgreen"),
    (colors.steelblue, "steelblue"),
    (colors.tan, "tan"),
    (colors.teal, "teal"),
    (colors.thistle, "thistle"),
    (colors.tomato, "tomato"),
    (colors.turquoise, "turquoise"),
    (colors.violet, "violet"),
    (colors.wheat, "wheat"),
    (colors.white, "white"),
    (colors.whitesmoke, "whitesmoke"),
    (colors.yellow, "yellow"),
    (colors.yellowgreen, "yellowgreen"),
]

# ファイル設定
outDir = "./colortest"
outFileName = "colortest"
outFileExt = "pdf"
path = "{0}/{1}.{2}".format(outDir, outFileName, outFileExt)
pdfFile = canvas.Canvas(path)
pdfFile.saveState()

pdfFile.setAuthor('relaxseason')
pdfFile.setTitle('印刷色テスト用')
pdfFile.setSubject('印刷色テスト用')

# A4
a4width = 210
a4height = 297
pdfFile.setPageSize((a4width*mm, a4height*mm))

# 余白
xmargin = 5
ymargin = xmargin

# 10 x 15の配置、xは0.5mm, yは1mm　余白をとる
outerCellMargin_x = 0.5
outerCellMargin_y = 1
outerCellCount_x = 10
outerCellCount_y = 15
outerCellWidth = (a4width-xmargin*2)/outerCellCount_x
outerCellHeight = (a4height - ymargin*2)/outerCellCount_y
innerCellMargin_side = outerCellWidth / 6
innerCellMargin_bottom = outerCellHeight / 4


for i, color in [(i, j) for (i, j) in enumerate(colorlist)]:
    # ラインの色指定
    pdfFile.setStrokeColor(color[0])
    colorName = color[1]

    # 表の描画位置
    cell_x = i % outerCellCount_x
    cell_y = i // outerCellCount_x
    # 外側のセル設定
    pdfFile.setLineWidth(0.1*mm)
    offset_x = xmargin + cell_x * outerCellWidth + outerCellMargin_x
    offset_y = ymargin + cell_y * outerCellHeight + outerCellMargin_y
    width = outerCellWidth - outerCellMargin_x * 2
    height = outerCellHeight - outerCellMargin_y * 2
    pdfFile.rect(offset_x * mm, offset_y * mm, width * mm, height * mm)

    # 色名表示
    pdfFile.setFont("Times-Roman", 6)
    pdfFile.setFillColor(colors.black)
    name_x = offset_x
    name_y = offset_y + 1
    pdfFile.drawString(name_x * mm, name_y * mm, colorName)

    # 内側のセル設定
    pdfFile.setLineWidth(1)
    innerOffset_x = offset_x + innerCellMargin_side
    innerOffset_y = offset_y + innerCellMargin_bottom
    innerWidth = width - innerCellMargin_side * 2
    innerHeight = height - innerCellMargin_bottom
    pdfFile.rect(innerOffset_x * mm, innerOffset_y *
                 mm, innerWidth * mm, innerHeight * mm)

    # 第1
    # 1ページ目
    pdfFile.setFillColor(color[0])
    dotspace1st = 1.25
    for x, y in [((x)*dotspace1st, (y)*dotspace1st)
                 for x in range(math.ceil(innerWidth / dotspace1st))
                 for y in range(math.ceil(innerHeight / dotspace1st))]:
        pdfFile.circle((innerOffset_x + x) * mm,
                       (innerOffset_y + y) * mm,
                       0.15*mm, stroke=0, fill=1)

    # 第2
    # 1ページ目
    pdfFile.setFillColor(color[0])
    dotspace2nd = 5
    for x, y in [((x)*dotspace2nd, (y)*dotspace2nd)
                 for x in range(math.ceil(innerWidth / dotspace2nd))
                 for y in range(math.ceil(innerHeight / dotspace2nd))]:
        pdfFile.circle((innerOffset_x + x) * mm,
                       (innerOffset_y + y) * mm,
                       0.25*mm, stroke=0, fill=1)

pdfFile.restoreState()
pdfFile.save()
