# -*- coding:utf-8 -*-
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.pdfbase.ttfonts import TTFont
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
# colorsList = [
#     (colors.olive, "olive")
# ]
for color, colorName in colorsList:
    # 出力先設定
    outPath = "./pdf/A5Slim-Dot-Daily-Color"
    outFileName = "A5Slim-Daily"
    outFileExt = "pdf"
    path = "{0}/{1}-{2}.{3}".format(outPath,
                                    outFileName, colorName, outFileExt)
    pdfFile = canvas.Canvas(path)
    pdfFile.saveState()

    pdfFile.setAuthor('relaxseason')
    pdfFile.setTitle('A4 Slim 1.25ドット日記')
    pdfFile.setSubject('A4 Slim 1.25ドット日記')

    # A4
    a4height = 210
    a4width = 297
    pdfFile.setPageSize((a4width*mm, a4height*mm))

    # ラインの色指定
    linecolor = color
    # linecolor = colors.green
    pdfFile.setStrokeColor(linecolor)
    # pdfFile.setFillColorRGB(128, 128, 128)

    # ラインの太さを変更する
    pdfFile.setLineWidth(0.01*mm)

    # A5 slimサイズ(210x99)にラインを入れる
    page_width = 99
    pdfFile.line(0, 0, 0, a4height*mm)
    pdfFile.line(page_width*1*mm, 0, page_width*1*mm, a4height * mm)
    pdfFile.line(page_width*2*mm, 0, page_width*2*mm, a4height * mm)
    pdfFile.line(page_width*3*mm, 0, page_width*3*mm, a4height * mm)

    # ドット方眼
    pdfFile.setFillColor(linecolor)
    dotspace1st = 1.25
    dotsize1st = 0.1
    points1st = [((x)*dotspace1st, (y)*dotspace1st)
                 for x in range(math.ceil(page_width/dotspace1st))
                 for y in range(math.ceil(a4height/dotspace1st)+1)]
    for x, y in points1st:
        pdfFile.circle((x+page_width*0)*mm, y*mm,
                       dotsize1st*mm, stroke=0, fill=1)
        pdfFile.circle((x+page_width*1)*mm, y*mm,
                       dotsize1st*mm, stroke=0, fill=1)
        pdfFile.circle((x+page_width*2)*mm, y*mm,
                       dotsize1st*mm, stroke=0, fill=1)

    dotspace2nd = 5
    dotsize2nd = 0.2
    points2nd = [((x)*dotspace2nd, (y)*dotspace2nd)
                 for x in range(math.ceil(page_width/dotspace2nd))
                 for y in range(math.ceil(a4height/dotspace2nd)+1)]
    for x, y in points2nd:
        pdfFile.circle((x+page_width*0)*mm, y*mm,
                       dotsize2nd*mm, stroke=0, fill=1)
        pdfFile.circle((x+page_width*1)*mm, y*mm,
                       dotsize2nd*mm, stroke=0, fill=1)
        pdfFile.circle((x+page_width*2)*mm, y*mm,
                       dotsize2nd*mm, stroke=0, fill=1)
    # 日付領域
    header_mergin_top = 5
    header_mergin_left = 5
    header_mergin_bottom = 5
    header_mark_height = 5
    header_mark_width = 5
    pdfFile.setLineWidth(0.4*mm)
    pdfFile.rect((header_mergin_left+page_width*0) * mm,
                 (a4height - (header_mergin_top+header_mark_height)) * mm,
                 (header_mark_width) * mm,
                 (header_mark_height) * mm)
    pdfFile.rect((header_mergin_left+page_width*1) * mm,
                 (a4height - (header_mergin_top+header_mark_height)) * mm,
                 (header_mark_width) * mm,
                 (header_mark_height) * mm)
    pdfFile.rect((header_mergin_left+page_width*2) * mm,
                 (a4height - (header_mergin_top+header_mark_height)) * mm,
                 (header_mark_width) * mm,
                 (header_mark_height) * mm)

    # タイムライン
    interval = 5
    timeline_mergin_left = 10
    division_size = dotspace1st
    timeline_head = a4height - \
        (header_mergin_top + header_mark_height + header_mergin_bottom)

    pdfFile.line((timeline_mergin_left+page_width*0) * mm,
                 timeline_head * mm,
                 (timeline_mergin_left+page_width*0) * mm,
                 (timeline_head - interval * 23) * mm)
    pdfFile.line((timeline_mergin_left+page_width*1) * mm,
                 timeline_head * mm,
                 (timeline_mergin_left+page_width*1) * mm,
                 (timeline_head - interval * 23) * mm)
    pdfFile.line((timeline_mergin_left+page_width*2) * mm,
                 timeline_head * mm,
                 (timeline_mergin_left+page_width*2) * mm,
                 (timeline_head - interval * 23) * mm)

    lines = [((timeline_mergin_left-division_size+page_width*0)*mm,
              (timeline_head-y*interval)*mm,
              (timeline_mergin_left+division_size+page_width*0)*mm,
              (timeline_head-y*interval)*mm) for y in range(24)]
    lines2 = [((timeline_mergin_left-division_size+page_width*1)*mm,
               (timeline_head-y*interval)*mm,
               (timeline_mergin_left+division_size+page_width*1)*mm,
               (timeline_head-y*interval)*mm) for y in range(24)]
    lines3 = [((timeline_mergin_left-division_size+page_width*2)*mm,
               (timeline_head-y*interval)*mm,
               (timeline_mergin_left+division_size+page_width*2)*mm,
               (timeline_head-y*interval)*mm) for y in range(24)]
    pdfFile.lines(lines+lines2+lines3)

    # タイムラインの数値
    # フォント登録
    fontfile = './fonts/GenShinGothic-Normal.ttf'
    fontname = 'GenShinGothic'
    pdfmetrics.registerFont(TTFont(fontname, fontfile))
    font_size = 7
    pdfFile.setFont(fontname, font_size)
    pdfFile.setFillColor(colors.black)

    # 描画位置
    time_x = timeline_mergin_left - (division_size + dotspace1st)
    time_head = timeline_head - (dotspace1st)
    # 表示テキスト
    times = ["{:02}".format(x) for x in (list(range(5, 23))+list(range(6)))]
    for i, time in enumerate(times):
        pdfFile.drawRightString(
            (time_x+page_width*0) * mm,  (time_head - interval * i) * mm, time)
        pdfFile.drawRightString(
            (time_x+page_width*1) * mm,  (time_head - interval * i) * mm, time)
        pdfFile.drawRightString(
            (time_x+page_width*2) * mm,  (time_head - interval * i) * mm, time)

    pdfFile.restoreState()
    pdfFile.save()
