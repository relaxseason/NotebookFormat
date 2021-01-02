# -*- coding:utf-8 -*-
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
from reportlab.lib import colors
from logging import getLogger
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
# pdfFile.setFillColor(colors.green)
pdfFile.setStrokeColor(colors.blue)
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

# M9用の9マスを追加する
# M9のラインの太さを変更する
pdfFile.setLineWidth(1)

# 表の描画

base_x_space = 3
base_y_space = 29.25
cellwidth = 28
base_points = [{"x": 0, "y": 0}, {"x": d3width, "y": 0}, {
    "x": 0, "y": half_height}, {"x": d3width, "y": half_height}]
for base in base_points:
    x_space = base_x_space + base["x"]
    y_space = base_y_space + base["y"]
    xlist = ((x_space + cellwidth * 0) * mm, (x_space + cellwidth * 1) *
             mm, (x_space + cellwidth * 2) * mm, (x_space + cellwidth * 3) * mm)
    ylist = ((y_space + cellwidth * 0) * mm, (y_space + cellwidth * 1) *
             mm, (y_space + cellwidth * 2) * mm, (y_space + cellwidth * 3) * mm)
    pdfFile.grid(xlist, ylist)

pdfFile.restoreState()
pdfFile.save()
