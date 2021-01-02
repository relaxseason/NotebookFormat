# -*- coding:utf-8 -*-
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
from reportlab.lib import colors
from logging import getLogger
logger = getLogger(__name__)


outPath = "./pdf"
outFileName = "A4-M81B"
outFileExt = "pdf"
pdfFile = canvas.Canvas("{0}/{1}.{2}".format(outPath, outFileName, outFileExt))
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
# pdfFile.setFillColor(colors.green)
pdfFile.setStrokeColor(colors.blue)
# pdfFile.setFillColorRGB(128, 128, 128)

# ラインの太さを変更する
pdfFile.setLineWidth(0.1*mm)

# M9用の9マスを追加する


# 表の描画

cellwidth = 21.5
base_x_space = (a4width - (cellwidth * 9))/2
base_y_space = (a4height - (cellwidth * 9))/2
# 8個の曼陀羅
base_points = [{"x": base_x_space + cellwidth * 0 * 3,
                "y": base_y_space + cellwidth * 0 * 3},
               {"x": base_x_space + cellwidth * 1 * 3,
                "y": base_y_space + cellwidth * 0 * 3},
               {"x": base_x_space + cellwidth * 2 * 3,
                "y": base_y_space + cellwidth * 0 * 3},
               {"x": base_x_space + cellwidth * 0 * 3,
                "y": base_y_space + cellwidth * 1 * 3},
               # {"x": base_x_space + cellwidth * 1 * 3,
               # "y": base_y_space + cellwidth * 1 * 3},
               {"x": base_x_space + cellwidth * 2 * 3,
                "y": base_y_space + cellwidth * 1 * 3},
               {"x": base_x_space + cellwidth * 0 * 3,
                "y": base_y_space + cellwidth * 2 * 3},
               {"x": base_x_space + cellwidth * 1 * 3,
                "y": base_y_space + cellwidth * 2 * 3},
               {"x": base_x_space + cellwidth * 2 * 3,
                "y": base_y_space + cellwidth * 2 * 3},
               ]
for base in base_points:
    x_space = base["x"]
    y_space = base["y"]
    xlist = ((x_space + cellwidth * 0) * mm, (x_space + cellwidth * 1) *
             mm, (x_space + cellwidth * 2) * mm, (x_space + cellwidth * 3) * mm)
    ylist = ((y_space + cellwidth * 0) * mm, (y_space + cellwidth * 1) *
             mm, (y_space + cellwidth * 2) * mm, (y_space + cellwidth * 3) * mm)
    pdfFile.grid(xlist, ylist)

# 中央の曼陀羅
# ラインの太さを変更する
pdfFile.setLineWidth(1)
x_space = base_x_space
y_space = base_y_space
xlist = ((x_space + cellwidth * 3) * mm, (x_space + cellwidth * 4) * mm,
         (x_space + cellwidth * 5) * mm,  (x_space + cellwidth * 6) * mm)
ylist = (
    (y_space + cellwidth * 3) * mm, (y_space + cellwidth * 4) * mm,
    (y_space + cellwidth * 5) * mm, (y_space + cellwidth * 6) * mm)
pdfFile.grid(xlist, ylist)

pdfFile.restoreState()
pdfFile.save()
