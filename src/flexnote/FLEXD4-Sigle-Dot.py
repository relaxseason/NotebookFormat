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
    FIRST_DOT_INTERVAL = 1.25
    FIRST_DOT_SIZE = 0.1
    SECOND_DOT_INTERVAL = 5
    SECOND_DOT_SIZE = 0.2
    HEADER_TOP = SECOND_DOT_INTERVAL
    HEADER_LEFT = SECOND_DOT_INTERVAL
    HEADER_HEIGHT = SECOND_DOT_INTERVAL
    HEADER_WIDTH = SECOND_DOT_INTERVAL
    HEADER_BOTTOM = SECOND_DOT_INTERVAL
    FLEXD4_WIDTH = 120
    FLEXD4_HEIGHT = A4_LANDSCAPE_WIDTH/2

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

        out_file_name = self.format_name
        out_file_ext = "pdf"
        path = "{0}/{1}-{2}.{3}".format(
            out_path, out_file_name, color_name, out_file_ext)
        return path

    def set_property(self):
        if self.pdf_file is None:
            raise ValueError('pdf_file is not assigned')

        self.pdf_file.setAuthor('relaxseason')
        self.pdf_file.setTitle('Flex D4 Single 1.25ドット方眼')
        self.pdf_file.setSubject('Flex D4 Single 1.25ドット方眼')
        self.pdf_file.setPageSize(
            (self.FLEXD4_WIDTH * mm, self.FLEXD4_HEIGHT * mm))

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
        self.pdf_file.line(0, 0, 0, self.FLEXD4_HEIGHT * mm)
        self.pdf_file.line(self.FLEXD4_WIDTH * mm,
                           0,
                           self.FLEXD4_WIDTH * mm,
                           self.FLEXD4_HEIGHT * mm)

    def draw_first_dotgrid(self, color):
        if self.pdf_file is None:
            raise ValueError('pdf_file is not assigned')

        # ドット方眼
        self.pdf_file.setFillColor(color)
        points1st = [((x)*self.FIRST_DOT_INTERVAL, (y)*self.FIRST_DOT_INTERVAL)
                     for x in range(math.ceil(self.FLEXD4_WIDTH
                                              / self.FIRST_DOT_INTERVAL))
                     for y in range(math.ceil(self.FLEXD4_HEIGHT
                                              / self.FIRST_DOT_INTERVAL) + 1)]
        for x, y in points1st:
            self.pdf_file.circle((x + self.FLEXD4_WIDTH * 0) * mm,
                                 (self.FLEXD4_HEIGHT - y) * mm,
                                 self.FIRST_DOT_SIZE * mm, stroke=0, fill=1)

    def draw_second_dotgrid(self, color):
        if self.pdf_file is None:
            raise ValueError('pdf_file is not assigned')
        # ドット方眼
        self.pdf_file.setFillColor(color)
        points2nd = [((x) * self.SECOND_DOT_INTERVAL,
                      (y) * self.SECOND_DOT_INTERVAL)
                     for x in range(math.ceil(self.FLEXD4_WIDTH
                                              / self.SECOND_DOT_INTERVAL))
                     for y in range(math.ceil(self.FLEXD4_HEIGHT
                                              / self.SECOND_DOT_INTERVAL) + 1)]
        for x, y in points2nd:
            self.pdf_file.circle((x + self.FLEXD4_WIDTH * 0) * mm,
                                 (self.FLEXD4_HEIGHT - y) * mm,
                                 self.SECOND_DOT_SIZE * mm, stroke=0, fill=1)

    def write_pdf_file(self, color_name):
        if self.pdf_file is None:
            raise ValueError('pdf_file is not assigned')
        self.pdf_file.restoreState()
        self.pdf_file.save()
        print("Save:{0}".format(color_name))

    def create_format(self, color, color_name):
        out_path = self.create_out_path(color_name)
        self.pdf_file = canvas.Canvas(out_path)
        self.pdf_file.saveState()
        self.set_property()
        self.draw_split_line(color)
        self.draw_first_dotgrid(color)
        self.draw_second_dotgrid(color)
        self.write_pdf_file(color_name)

    def create_format_all_color(self):
        for color, color_name in self.color_list:
            self.create_format(color, color_name)


if __name__ == "__main__":
    format = BaseNoteFormat("FlexD4SingleDot")
    # format.create_format(colors.green, "green")
    format.create_format_all_color()
