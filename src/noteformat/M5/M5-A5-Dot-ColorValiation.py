# -*- coding:utf-8 -*-
import os
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
from reportlab.lib import colors
from logging import getLogger
import math
logger = getLogger(__name__)


class BaseNoteFormat:

    # 用紙サイズ
    A4_LANDSCAPE_X = 297
    A4_LANDSCAPE_Y = 210
    A4_PORTRAIT_X = A4_LANDSCAPE_Y
    A4_PORTRAIT_Y = A4_LANDSCAPE_X
    A5_LANDSCAPE_WIDTH = 148
    A5_LANDSCAPE_HEIGHT = 210
    A5_PORTRAIT_WIDTH = A5_LANDSCAPE_HEIGHT
    A5_PORTRAIT_HEIGHT = A5_LANDSCAPE_WIDTH

    M5_LANDSCAPE_X = 105
    M5_LANDSCAPE_Y = 62
    M5_PORTLAIT_X = M5_LANDSCAPE_Y
    M5_PORTLAIT_Y = M5_LANDSCAPE_X
    A4SLIM_LANDSCAPE_X = 210
    A4SLIM_LANDSCAPE_Y = 99
    A4SLIM_PORTRAIT_X = A4SLIM_LANDSCAPE_Y
    A4SLIM_PORTRAIT_Y = A4SLIM_LANDSCAPE_X

    # # 印刷対象のサイズ
    # BASE_PAGE_X = A4_LANDSCAPE_X
    # BASE_PAGE_Y = A4_LANDSCAPE_Y
    # # 切り出す1枚のサイズ()
    # TARGET_PAGE_X = M5_PORTLAIT_X
    # TARGET_PAGE_Y = M5_PORTLAIT_Y

    # A5の場合
    # 印刷対象のサイズ
    BASE_PAGE_X = A5_PORTRAIT_HEIGHT
    BASE_PAGE_Y = A5_PORTRAIT_WIDTH
    # 切り出す1枚のサイズ
    TARGET_PAGE_X = M5_PORTLAIT_X
    TARGET_PAGE_Y = M5_PORTLAIT_Y

    # タイトル
    PAGE_TITLE = 'M5 1.25ドット方眼'

    # ドット設定
    FIRST_DOT_INTERVAL = 1.25
    # FIRST_DOT_SIZE = 0.1
    FIRST_DOT_SIZE = 0.075
    SECOND_DOT_INTERVAL = 5
    # SECOND_DOT_SIZE = 0.2
    SECOND_DOT_SIZE = 0.15
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
        self.pdf_file.setTitle(self.PAGE_TITLE)
        self.pdf_file.setSubject(self.PAGE_TITLE)
        self.pdf_file.setPageSize(
            # (self.BASE_PAGE_X*mm, self.BASE_PAGE_Y*mm)
            # A5の場合
            (self.A4_LANDSCAPE_X*mm, self.A4_LANDSCAPE_Y*mm)
        )

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

        x_mergin = (self.BASE_PAGE_X % self.TARGET_PAGE_X)/2
        y_mergin = (self.BASE_PAGE_Y % self.TARGET_PAGE_Y)/2
        # 縦線のパラメータ
        params = [((x * self.TARGET_PAGE_X) + x_mergin, 0,
                   (x * self.TARGET_PAGE_X) + x_mergin, self.BASE_PAGE_Y)
                  for x in range(math.ceil(self.BASE_PAGE_X
                                           / self.TARGET_PAGE_X))]
        params += [[0, 0, 0, self.BASE_PAGE_Y]]
        params += [[self.BASE_PAGE_X, 0, self.BASE_PAGE_X, self.BASE_PAGE_Y]]
        # 横線のパラメータ
        params += [(0,    (y * self.TARGET_PAGE_Y) + y_mergin,
                    self.BASE_PAGE_X, (y * self.TARGET_PAGE_Y) + y_mergin)
                   for y in range(math.ceil(self.BASE_PAGE_Y
                                            / self.TARGET_PAGE_Y))]
        params += [[0, 0, self.BASE_PAGE_X, 0]]
        params += [[0, self.BASE_PAGE_Y, self.BASE_PAGE_X, self.BASE_PAGE_Y]]

        for x, y, width, height in params:
            # A5をA4として印刷させるため右に印刷
            dx = x + self.BASE_PAGE_X + 1
            dwidth = width + self.BASE_PAGE_X + 1
            self.pdf_file.line(dx * mm, y * mm, dwidth * mm, height * mm)

    def draw_first_dotgrid(self, color):
        if self.pdf_file is None:
            raise ValueError('pdf_file is not assigned')

        # ドット方眼
        self.pdf_file.setFillColor(color)
        x_mergin = (self.BASE_PAGE_X % self.TARGET_PAGE_X)/2
        y_mergin = (self.BASE_PAGE_Y % self.TARGET_PAGE_Y)/2

        points = [(
            (x * self.FIRST_DOT_INTERVAL
             + x_mergin + (dx * self.TARGET_PAGE_X)),
            (y * self.FIRST_DOT_INTERVAL
             + y_mergin + (dy * self.TARGET_PAGE_Y))
        )
            for x in range(
            math.ceil(self.TARGET_PAGE_X
                      / self.FIRST_DOT_INTERVAL))
            for y in range(
            math.ceil(self.TARGET_PAGE_Y
                      / self.FIRST_DOT_INTERVAL))
            for dx in range(
            math.floor(self.BASE_PAGE_X
                       / self.TARGET_PAGE_X))
            for dy in range(
            math.floor(self.BASE_PAGE_Y
                       / self.TARGET_PAGE_Y))
        ]
        for x, y in points:
            # A5をA4として印刷させるため右に印刷
            dx = x + self.BASE_PAGE_X + 1
            self.pdf_file.circle(
                dx * mm,
                (self.BASE_PAGE_Y - y) * mm,
                self.FIRST_DOT_SIZE * mm,
                stroke=0, fill=1
            )

    def draw_second_dotgrid(self, color):
        if self.pdf_file is None:
            raise ValueError('pdf_file is not assigned')
        self.pdf_file.setFillColor(color)

        # 余白
        x_mergin = (self.BASE_PAGE_X % self.TARGET_PAGE_X) / 2
        y_mergin = (self.BASE_PAGE_Y % self.TARGET_PAGE_Y) / 2

        # ドット方眼
        points = [(
            (x * self.SECOND_DOT_INTERVAL
             + x_mergin + (dx * self.TARGET_PAGE_X)),
            (y * self.SECOND_DOT_INTERVAL
             + y_mergin + (dy * self.TARGET_PAGE_Y))
        )
            for x in range(
                math.ceil(self.TARGET_PAGE_X
                          / self.SECOND_DOT_INTERVAL))
            for y in range(
                math.ceil(self.TARGET_PAGE_Y
                          / self.SECOND_DOT_INTERVAL))
            for dx in range(
                math.floor(self.BASE_PAGE_X
                           / self.TARGET_PAGE_X))
            for dy in range(
                math.floor(self.BASE_PAGE_Y
                           / self.TARGET_PAGE_Y))
        ]
        for x, y in points:
            # A5をA4として印刷させるため右に印刷
            dx = x + self.BASE_PAGE_X + 1
            self.pdf_file.circle(
                dx * mm,
                (self.BASE_PAGE_Y - y) * mm,
                self.SECOND_DOT_SIZE * mm,
                stroke=0, fill=1
            )

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

    def create_format_color_valiation(self):
        pass

    def create_format_all_color(self):
        for color, color_name in self.color_list:
            self.create_format(color, color_name)


if __name__ == "__main__":
    # format = BaseNoteFormat("M5-DotGrid")
    format = BaseNoteFormat("M5-A5-DotGrid")
    # format.create_format(colors.mediumslateblue, "mediumslateblue")
    format.create_format_all_color()
