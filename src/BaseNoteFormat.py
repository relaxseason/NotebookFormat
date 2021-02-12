# -*- coding:utf-8 -*-
import os
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.pdfbase.ttfonts import TTFont
from logging import getLogger
import math
logger = getLogger(__name__)


class BaseNoteFormat:
    A4_LANDSCAPE_WIDTH = 297
    A4_LANDSCAPE_HEIGHT = 210
    A4_PORTRAIT_WIDTH = 210
    A4_PORTRAIT_HEIGHT = 297
    A4SLIM_LANDSCAPE_WIDTH = 210
    A4SLIM_LANDSCAPE_HEIGHT = 99
    A4SLIM_PORTRAIT_WIDTH = 99
    A4SLIM_PORTRAIT_HEIGHT = 210
    FIRST_DOT_INTERVAL = 1
    FIRST_DOT_SIZE = 0.1
    SECOND_DOT_INTERVAL = 8
    SECOND_DOT_SIZE = 0.2
    HEADER_TOP = SECOND_DOT_INTERVAL
    HEADER_LEFT = SECOND_DOT_INTERVAL
    HEADER_HEIGHT = SECOND_DOT_INTERVAL
    HEADER_WIDTH = SECOND_DOT_INTERVAL
    HEADER_BOTTOM = SECOND_DOT_INTERVAL

    def __init__(self, format_name):
        self.pdf_file = None
        self.format_name = format_name
        self.color_list = [
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

    def create_out_path(self, color_name):
        # 出力先の作成
        out_path = "./pdf/{0}".format(self.format_name)
        if not os.path.exists(out_path):
            os.makedirs(out_path, exist_ok=True)

        out_file_name = "A5Slim-Daily"
        out_file_ext = "pdf"
        path = "{0}/{1}-{2}.{3}".format(
            out_path, out_file_name, color_name, out_file_ext)
        return path

    def set_property(self):
        if self.pdf_file is None:
            raise ValueError('pdf_file is not assigned')

        self.pdf_file.setAuthor('relaxseason')
        self.pdf_file.setTitle('A4 Slim 1.25ドット日記')
        self.pdf_file.setSubject('A4 Slim 1.25ドット日記')
        self.pdf_file.setPageSize(
            (self.A4_LANDSCAPE_WIDTH*mm, self.A4_LANDSCAPE_HEIGHT*mm))

    def set_color(self, color):
        if self.pdf_file is None:
            raise ValueError('pdf_file is not assigned')

        self.pdf_file.setStrokeColor(color)
        self.pdf_file.setFillColor(color)

    def draw_split_line(self, color):
        if self.pdf_file is None:
            raise ValueError('pdf_file is not assigned')

        self.pdf_file.setStrokeColor(color)
        self.pdf_file.setLineWidth(0.01*mm)

        # A5 slimサイズ(210x99)にラインを入れる
        self.pdf_file.line(0, 0, 0, self.A4SLIM_PORTRAIT_HEIGHT*mm)
        self.pdf_file.line(self.A4SLIM_PORTRAIT_WIDTH * 1 * mm,
                           0,
                           self.A4SLIM_PORTRAIT_WIDTH * 1 * mm,
                           self.A4SLIM_PORTRAIT_HEIGHT * mm)
        self.pdf_file.line(self.A4SLIM_PORTRAIT_WIDTH * 2 * mm,
                           0,
                           self.A4SLIM_PORTRAIT_WIDTH * 2 * mm,
                           self.A4SLIM_PORTRAIT_HEIGHT * mm)
        self.pdf_file.line(self.A4SLIM_PORTRAIT_WIDTH * 3 * mm,
                           0,
                           self.A4SLIM_PORTRAIT_WIDTH * 3 * mm,
                           self.A4SLIM_PORTRAIT_HEIGHT * mm)

    def draw_first_dotgrid(self, color):
        if self.pdf_file is None:
            raise ValueError('pdf_file is not assigned')

        # ドット方眼
        self.pdf_file.setFillColor(color)
        points1st = [((x)*self.FIRST_DOT_INTERVAL, (y)*self.FIRST_DOT_INTERVAL)
                     for x in range(math.ceil(self.A4SLIM_PORTRAIT_WIDTH
                                              / self.FIRST_DOT_INTERVAL))
                     for y in range(math.ceil(self.A4SLIM_PORTRAIT_HEIGHT
                                              / self.FIRST_DOT_INTERVAL) + 1)]
        for x, y in points1st:
            self.pdf_file.circle((x + self.A4SLIM_PORTRAIT_WIDTH * 0) * mm,
                                 (self.A4SLIM_PORTRAIT_HEIGHT - y) * mm,
                                 self.FIRST_DOT_SIZE * mm, stroke=0, fill=1)
            self.pdf_file.circle((x + self.A4SLIM_PORTRAIT_WIDTH * 1) * mm,
                                 (self.A4SLIM_PORTRAIT_HEIGHT - y) * mm,
                                 self.FIRST_DOT_SIZE * mm, stroke=0, fill=1)
            self.pdf_file.circle((x + self.A4SLIM_PORTRAIT_WIDTH * 2) * mm,
                                 (self.A4SLIM_PORTRAIT_HEIGHT - y) * mm,
                                 self.FIRST_DOT_SIZE * mm, stroke=0, fill=1)

    def draw_second_dotgrid(self, color):
        if self.pdf_file is None:
            raise ValueError('pdf_file is not assigned')
        # ドット方眼
        self.pdf_file.setFillColor(color)
        points2nd = [((x) * self.SECOND_DOT_INTERVAL,
                      (y) * self.SECOND_DOT_INTERVAL)
                     for x in range(math.ceil(self.A4SLIM_PORTRAIT_WIDTH
                                              / self.SECOND_DOT_INTERVAL))
                     for y in range(math.ceil(self.A4SLIM_PORTRAIT_HEIGHT
                                              / self.SECOND_DOT_INTERVAL) + 1)]
        for x, y in points2nd:
            self.pdf_file.circle((x + self.A4SLIM_PORTRAIT_WIDTH * 0) * mm,
                                 (self.A4SLIM_PORTRAIT_HEIGHT - y) * mm,
                                 self.SECOND_DOT_SIZE * mm, stroke=0, fill=1)
            self.pdf_file.circle((x + self.A4SLIM_PORTRAIT_WIDTH * 1) * mm,
                                 (self.A4SLIM_PORTRAIT_HEIGHT - y) * mm,
                                 self.SECOND_DOT_SIZE * mm, stroke=0, fill=1)
            self.pdf_file.circle((x + self.A4SLIM_PORTRAIT_WIDTH * 2) * mm,
                                 (self.A4SLIM_PORTRAIT_HEIGHT - y) * mm,
                                 self.SECOND_DOT_SIZE * mm, stroke=0, fill=1)

    def write_pdf_file(self, color_name):
        if self.pdf_file is None:
            raise ValueError('pdf_file is not assigned')
        self.pdf_file.restoreState()
        self.pdf_file.save()
        print("Save:{0}".format(color_name))

    def draw_daily_header(self, color):
        if self.pdf_file is None:
            raise ValueError('pdf_file is not assigned')
        # 日付領域
        header_mergin_top = self.HEADER_TOP
        header_mergin_left = self.HEADER_LEFT
        header_mark_height = self.HEADER_HEIGHT
        header_mark_width = self.HEADER_WIDTH
        self.pdf_file.setLineWidth(0.4*mm)
        self.pdf_file.rect(
            (header_mergin_left + self.A4SLIM_PORTRAIT_WIDTH * 0) * mm,
            (self.A4SLIM_PORTRAIT_HEIGHT -
             (header_mergin_top + header_mark_height)) * mm,
            (header_mark_width) * mm,
            (header_mark_height) * mm
        )
        self.pdf_file.rect(
            (header_mergin_left + self.A4SLIM_PORTRAIT_WIDTH * 1) * mm,
            (self.A4SLIM_PORTRAIT_HEIGHT -
             (header_mergin_top + header_mark_height)) * mm,
            (header_mark_width) * mm,
            (header_mark_height) * mm
        )
        self.pdf_file.rect(
            (header_mergin_left + self.A4SLIM_PORTRAIT_WIDTH * 2) * mm,
            (self.A4SLIM_PORTRAIT_HEIGHT -
             (header_mergin_top + header_mark_height)) * mm,
            (header_mark_width) * mm,
            (header_mark_height) * mm
        )

    def draw_daily_timeline(self, color_name):
        # タイムライン
        interval = self.SECOND_DOT_INTERVAL
        timeline_mergin_left = self.SECOND_DOT_INTERVAL * 2
        division_size = self.FIRST_DOT_INTERVAL
        timeline_head = self.A4SLIM_PORTRAIT_HEIGHT - \
            (self.HEADER_TOP + self.HEADER_HEIGHT + self.HEADER_BOTTOM)

        self.pdf_file.line(
            (timeline_mergin_left + self.A4SLIM_PORTRAIT_WIDTH * 0) * mm,
            timeline_head * mm,
            (timeline_mergin_left +
             self.A4SLIM_PORTRAIT_WIDTH * 0) * mm,
            (timeline_head - interval * 23) * mm
        )
        self.pdf_file.line(
            (timeline_mergin_left + self.A4SLIM_PORTRAIT_WIDTH * 1) * mm,
            timeline_head * mm,
            (timeline_mergin_left +
             self.A4SLIM_PORTRAIT_WIDTH * 1) * mm,
            (timeline_head - interval * 23) * mm
        )
        self.pdf_file.line(
            (timeline_mergin_left + self.A4SLIM_PORTRAIT_WIDTH * 2) * mm,
            timeline_head * mm,
            (timeline_mergin_left +
             self.A4SLIM_PORTRAIT_WIDTH * 2) * mm,
            (timeline_head - interval * 23) * mm
        )

        lines = [
            ((timeline_mergin_left - division_size
              + self.A4SLIM_PORTRAIT_WIDTH * 0) * mm,
             (timeline_head - y * interval) * mm,
             (timeline_mergin_left + division_size
              + self.A4SLIM_PORTRAIT_WIDTH * 0) * mm,
             (timeline_head - y * interval) * mm) for y in range(24)
        ]
        lines2 = [
            ((timeline_mergin_left - division_size
              + self.A4SLIM_PORTRAIT_WIDTH * 1) * mm,
             (timeline_head - y * interval) * mm,
             (timeline_mergin_left + division_size
              + self.A4SLIM_PORTRAIT_WIDTH * 1) * mm,
             (timeline_head - y * interval) * mm) for y in range(24)
        ]
        lines3 = [
            ((timeline_mergin_left-division_size
              + self.A4SLIM_PORTRAIT_WIDTH * 2) * mm,
             (timeline_head - y * interval) * mm,
             (timeline_mergin_left+division_size
              + self.A4SLIM_PORTRAIT_WIDTH * 2) * mm,
             (timeline_head - y * interval) * mm) for y in range(24)
        ]
        self.pdf_file.lines(lines + lines2 + lines3)

        # タイムラインの数値
        # フォント登録
        fontfile = './fonts/GenShinGothic-Normal.ttf'
        fontname = 'GenShinGothic'
        pdfmetrics.registerFont(TTFont(fontname, fontfile))
        font_size = 7
        self.pdf_file.setFont(fontname, font_size)
        self.pdf_file.setFillColor(colors.black)

        # 描画位置
        time_x = timeline_mergin_left - \
            (division_size + self.FIRST_DOT_INTERVAL)
        time_head = timeline_head - (self.FIRST_DOT_INTERVAL)
        # 表示テキスト
        times = ["{:02}".format(x)
                 for x in (list(range(5, 23))+list(range(6)))]
        for i, time in enumerate(times):
            self.pdf_file.drawRightString(
                (time_x + self.A4SLIM_PORTRAIT_WIDTH * 0) * mm,
                (time_head - interval * i) * mm, time)
            self.pdf_file.drawRightString(
                (time_x + self.A4SLIM_PORTRAIT_WIDTH * 1) * mm,
                (time_head - interval * i) * mm, time)
            self.pdf_file.drawRightString(
                (time_x + self.A4SLIM_PORTRAIT_WIDTH * 2) * mm,
                (time_head - interval * i) * mm, time)

    def create_format(self, color, color_name):
        out_path = self.create_out_path(color_name)
        self.pdf_file = canvas.Canvas(out_path)
        self.pdf_file.saveState()
        self.set_property()
        self.draw_split_line(color)
        self.draw_first_dotgrid(color)
        self.draw_second_dotgrid(color)
        self.draw_daily_header(color)
        self.draw_daily_timeline(color)
        self.write_pdf_file(color_name)

    def create_format_all_color(self):
        for color, color_name in self.color_list:
            self.create_format(color, color_name)


if __name__ == "__main__":
    format = BaseNoteFormat("BaseTest")
    # format.create_format(colors.green, "green")
    format.create_format_all_color()
