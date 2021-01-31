# -*- coding:utf-8 -*-
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
from reportlab.lib import colors
from logging import getLogger
import os
logger = getLogger(__name__)


outDir = "./pdf/M9"
if not os.path.exists(outDir):
    os.makedirs(outDir, exist_ok=True)

outFileName = "A4-M81A"
outFileExt = "pdf"
pdfFile = canvas.Canvas("{0}/{1}.{2}".format(outDir, outFileName, outFileExt))
pdfFile.saveState()

pdfFile.setAuthor('relaxseason')
pdfFile.setTitle('A4用 M81罫A')
pdfFile.setSubject('A4用 M81罫A')

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
pdfFile.setLineWidth(1)
# pdfFile.setLineWidth(0.1*mm)

# M9用の9マスを追加する
cellwidth = 21.5
m81width = 210
m81height = 210
base_x_space = (m81width - (cellwidth * 9))/2
base_y_space = (m81height - (cellwidth * 9))/2

# 8個の曼陀羅
base_points = [{"x": base_x_space + cellwidth * 0 * 3,
                "y": base_y_space + cellwidth * 0 * 3},
               ]
for base in base_points:
    x_space = base["x"]
    y_space = base["y"]
    xlist = (
        (x_space + cellwidth * 0) * mm,
        (x_space + cellwidth * 1) * mm,
        (x_space + cellwidth * 2) * mm,
        (x_space + cellwidth * 3) * mm,
        (x_space + cellwidth * 4) * mm,
        (x_space + cellwidth * 5) * mm,
        (x_space + cellwidth * 6) * mm,
        (x_space + cellwidth * 7) * mm,
        (x_space + cellwidth * 8) * mm,
        (x_space + cellwidth * 9) * mm,
    )
    ylist = (
        (y_space + cellwidth * 0) * mm,
        (y_space + cellwidth * 1) * mm,
        (y_space + cellwidth * 2) * mm,
        (y_space + cellwidth * 3) * mm,
        (y_space + cellwidth * 4) * mm,
        (y_space + cellwidth * 5) * mm,
        (y_space + cellwidth * 6) * mm,
        (y_space + cellwidth * 7) * mm,
        (y_space + cellwidth * 8) * mm,
        (y_space + cellwidth * 9) * mm,
    )
    pdfFile.grid(xlist, ylist)

# 切り取り線
pdfFile.setLineWidth(0.1*mm)
pdfFile.line(0, m81height * mm,
             m81width * mm, m81height * mm)

# PDF保存
pdfFile.restoreState()
pdfFile.save()
