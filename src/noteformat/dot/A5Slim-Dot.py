# -*- coding:utf-8 -*-
import os
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
from reportlab.lib import colors
from logging import getLogger
import math
logger = getLogger(__name__)


class BaseNoteFormat:
    A4_LANDSCAPE_WIDTH = 297
    A4_LANDSCAPE_HEIGHT = 210
    A4_PORTRAIT_WIDTH = 210
    A4_PORTRAIT_HEIGHT = 297

    A5_LANDSCAPE_WIDTH = 148
    A5_LANDSCAPE_HEIGHT = 210
    A5_PORTRAIT_WIDTH = 210
    A5_PORTRAIT_HEIGHT = 148

    A6_LANDSCAPE_WIDTH = 148
    A6_LANDSCAPE_HEIGHT = 105
    A6_PORTRAIT_WIDTH = 105
    A6_PORTRAIT_HEIGHT = 148

    A4SLIM_LANDSCAPE_WIDTH = 210
    A4SLIM_LANDSCAPE_HEIGHT = 99
    A4SLIM_PORTRAIT_WIDTH = 99
    A4SLIM_PORTRAIT_HEIGHT = 210

    A5SLIM_LANDSCAPE_WIDTH = 148
    A5SLIM_LANDSCAPE_HEIGHT = 70
    A5SLIM_PORTRAIT_WIDTH = 70
    A5SLIM_PORTRAIT_HEIGHT = 148

    A6SLIM_LANDSCAPE_WIDTH = 105
    A6SLIM_LANDSCAPE_HEIGHT = 49
    A6SLIM_PORTRAIT_WIDTH = 49
    A6SLIM_PORTRAIT_HEIGHT = 105

    FIRST_DOT_INTERVAL = 1.25
    FIRST_DOT_SIZE = 0.1
    SECOND_DOT_INTERVAL = 5
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
            # (colors.gainsboro, "gainsboro"),
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
            # (colors.peachpuff, "peachpuff"),
            # (colors.powderblue, "powderblue"),
            # (colors.silver, "silver"),
            # (colors.tan, "tan"),
            # (colors.thistle, "thistle"),
            # (colors.wheat, "wheat"),
            (colors.turquoise, "turquoise"),
            (colors.skyblue, "skyblue"),
            (colors.slateblue, "slateblue"),
            (colors.slategray, "slategray"),
            (colors.mediumslateblue, "mediumslateblue"),
            (colors.HexColor("#00687C"), "nandoiro"),
            (colors.HexColor("#45DDEE"), "_45DDEE"),  # 45DDEE 色名なし
            (colors.HexColor("#00687C"), "_納戸色"),  # なんどいろ
            (colors.HexColor("#00859B"), "_浅葱色"),  # あさぎいろ
            (colors.HexColor("#1D417A"), "_瑠璃紺"),  # るりこん
            (colors.HexColor("#6AA89D"), "_青竹色"),  # あおたけいろ
            (colors.HexColor("#242550"), "_青褐"),  # あおかち
            (colors.HexColor("#4D7198"), "_深毛月色"),  # シェンマオユエスー
            (colors.HexColor("#75C6C3"), "_白群1"),  # びゃくぐん
            (colors.HexColor("#73B3C1"), "_白群2"),  # びゃくぐん
            # JIS慣用色名
            (colors.HexColor("#84B5CF"), "_白群（びゃくぐん）"),
            (colors.HexColor("#5F836D"), "_緑青（ろくしょう）色"),
            (colors.HexColor("#49A581"), "_若竹色"),
            (colors.HexColor("#357C4C"), "_常磐（ときわ）色"),
            (colors.HexColor("#A09BD8"), "_藤色"),
            (colors.HexColor("#948BDB"), "_藤紫"),
            (colors.HexColor("#0090A8"), "_青緑"),
            (colors.HexColor("#47384F"), "_なす紺"),
            (colors.HexColor("#4A49AD"), "_ききょう色"),
            (colors.HexColor("#414FA3"), "_群青（ぐんじょう）色"),
            (colors.HexColor("#3451A4"), "_るり色"),
            (colors.HexColor("#2E4B71"), "_藍色"),
            (colors.HexColor("#95C0EC"), "_空色"),
            (colors.HexColor("#0087AA"), "_浅葱（あさぎ）色"),
            (colors.HexColor("#B13546"), "_茜色"),
            (colors.HexColor("#E54848"), "_緋色"),
            (colors.HexColor("#FF7F50"), "_珊瑚色"),
            (colors.HexColor("#77B8DA"), "_勿忘草色"),
            (colors.HexColor("#4169E1"), "_ロイヤル・ブルー"),
            (colors.HexColor("#5BB3B5"), "_新橋色"),
            (colors.HexColor("#97A61E"), "_萌黄"),
            (colors.HexColor("#A7663B"), "_琥珀色"),
        ]

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
        self.pdf_file.setTitle('A4 Slim 1.25ドット方眼')
        self.pdf_file.setSubject('A4 Slim 1.25ドット方眼')
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

        # 余白設定
        width_margin = (self.A4_LANDSCAPE_WIDTH %
                        self.A5SLIM_LANDSCAPE_WIDTH) / 2
        height_margin = (self.A4_LANDSCAPE_HEIGHT %
                         self.A5SLIM_LANDSCAPE_HEIGHT) / 2

        # 余白のラインを入れる(縦・横)

        # 左縦線
        left = (0 + width_margin)
        self.pdf_file.line(
            left * mm,
            0 * mm,
            left * mm,
            self.A4_LANDSCAPE_HEIGHT * mm
        )
        # 右縦線
        right = (self.A4_LANDSCAPE_WIDTH - width_margin)
        self.pdf_file.line(
            right * mm,
            0 * mm,
            right * mm,
            self.A4_LANDSCAPE_HEIGHT * mm
        )
        # 下横線
        bottom = (0 + height_margin)
        self.pdf_file.line(
            0 * mm,
            bottom * mm,
            self.A4_LANDSCAPE_WIDTH * mm,
            bottom * mm
        )
        # 上横線
        top = (self.A4_LANDSCAPE_HEIGHT - height_margin)
        self.pdf_file.line(
            0 * mm,
            top * mm,
            self.A4_LANDSCAPE_WIDTH * mm,
            top * mm
        )

        # A5縦の位置にラインを入れる
        for x in [(
            (x+1) * self.A5SLIM_LANDSCAPE_WIDTH) + width_margin
            for x in range(
            math.floor(self.A4_LANDSCAPE_WIDTH
                       / self.A5SLIM_LANDSCAPE_WIDTH)-1
        )]:
            self.pdf_file.line(
                x * mm,
                0 * mm,
                x * mm,
                self.A4_LANDSCAPE_HEIGHT * mm
            )

        # A5 slimサイズ(148x70)の横線を入れる
        for y in [(
            (y+1) * self.A5SLIM_LANDSCAPE_HEIGHT) + height_margin
            for y in range(
            math.floor(
                self.A4_LANDSCAPE_HEIGHT
                / self.A5SLIM_LANDSCAPE_HEIGHT) - 1
        )]:
            self.pdf_file.line(
                0,
                y * mm,
                self.A4_LANDSCAPE_WIDTH * mm,
                y * mm
            )

    def draw_dotgrid(self, color, interval, dotsize, offset=0):
        if self.pdf_file is None:
            raise ValueError('pdf_file is not assigned')

        # ドット方眼 (0からなので、)
        self.pdf_file.setFillColor(color)
        points = [((x) * interval + offset,
                   (y) * interval + offset)
                  for x in range(
                      math.floor((self.A5SLIM_LANDSCAPE_WIDTH - offset)
                                 / interval)+1)
                  for y in range(
                      math.floor((self.A5SLIM_LANDSCAPE_HEIGHT - offset)
                                 / interval)+1)]
        for x, y in points:
            self.pdf_file.circle((x + self.A5SLIM_LANDSCAPE_WIDTH * 0) * mm,
                                 (y + self.A5SLIM_LANDSCAPE_HEIGHT * 0) * mm,
                                 dotsize * mm, stroke=0, fill=1)
            self.pdf_file.circle((x + self.A5SLIM_LANDSCAPE_WIDTH * 1) * mm,
                                 (y + self.A5SLIM_LANDSCAPE_HEIGHT * 0) * mm,
                                 dotsize * mm, stroke=0, fill=1)
            self.pdf_file.circle((x + self.A5SLIM_LANDSCAPE_WIDTH * 0) * mm,
                                 (y + self.A5SLIM_LANDSCAPE_HEIGHT * 1) * mm,
                                 dotsize * mm, stroke=0, fill=1)
            self.pdf_file.circle((x + self.A5SLIM_LANDSCAPE_WIDTH * 1) * mm,
                                 (y + self.A5SLIM_LANDSCAPE_HEIGHT * 1) * mm,
                                 dotsize * mm, stroke=0, fill=1)
            self.pdf_file.circle((x + self.A5SLIM_LANDSCAPE_WIDTH * 0) * mm,
                                 (y + self.A5SLIM_LANDSCAPE_HEIGHT * 2) * mm,
                                 dotsize * mm, stroke=0, fill=1)
            self.pdf_file.circle((x + self.A5SLIM_LANDSCAPE_WIDTH * 1) * mm,
                                 (y + self.A5SLIM_LANDSCAPE_HEIGHT * 2) * mm,
                                 dotsize * mm, stroke=0, fill=1)

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
        self.draw_dotgrid(color, self.FIRST_DOT_INTERVAL, self.FIRST_DOT_SIZE)
        self.draw_dotgrid(color, self.SECOND_DOT_INTERVAL,
                          self.SECOND_DOT_SIZE, self.FIRST_DOT_INTERVAL)
        self.write_pdf_file(color_name)

    def create_format_all_color(self):
        for color, color_name in self.color_list:
            self.create_format(color, color_name)


if __name__ == "__main__":
    format = BaseNoteFormat("A5SlimDotGrid")
    format.create_format(colors.HexColor("#84B5CF"), "_白群（びゃくぐん）"),
    # format.create_format_all_color()
