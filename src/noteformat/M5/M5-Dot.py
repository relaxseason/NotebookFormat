# -*- coding:utf-8 -*-
import os
from typing import NamedTuple, Tuple
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
from reportlab.lib import colors
from logging import getLogger
import math
logger = getLogger(__name__)


class Margin(NamedTuple):
    width: float
    height: float


class BaseNoteFormat:
    TITLE = 'M5 1.25mmドット方眼'
    DIRNAME = 'M5DotGrid'
    A4_LANDSCAPE_WIDTH = 297
    A4_LANDSCAPE_HEIGHT = 210
    A4_PORTRAIT_WIDTH = A4_LANDSCAPE_HEIGHT
    A4_PORTRAIT_HEIGHT = A4_LANDSCAPE_WIDTH

    A5_LANDSCAPE_WIDTH = 148
    A5_LANDSCAPE_HEIGHT = 210
    A5_PORTRAIT_WIDTH = A5_LANDSCAPE_HEIGHT
    A5_PORTRAIT_HEIGHT = A5_LANDSCAPE_WIDTH

    A6_LANDSCAPE_WIDTH = 148
    A6_LANDSCAPE_HEIGHT = 105
    A6_PORTRAIT_WIDTH = A6_LANDSCAPE_HEIGHT
    A6_PORTRAIT_HEIGHT = A6_LANDSCAPE_WIDTH

    A7_LANDSCAPE_WIDTH = 105
    A7_LANDSCAPE_HEIGHT = 74
    A7_PORTRAIT_WIDTH = A7_LANDSCAPE_HEIGHT
    A7_PORTRAIT_HEIGHT = A7_LANDSCAPE_WIDTH

    A4SLIM_LANDSCAPE_WIDTH = 210
    A4SLIM_LANDSCAPE_HEIGHT = 99
    A4SLIM_PORTRAIT_WIDTH = A4SLIM_LANDSCAPE_HEIGHT
    A4SLIM_PORTRAIT_HEIGHT = A4SLIM_LANDSCAPE_WIDTH

    A5SLIM_LANDSCAPE_WIDTH = 148
    A5SLIM_LANDSCAPE_HEIGHT = 70
    A5SLIM_PORTRAIT_WIDTH = A5SLIM_LANDSCAPE_HEIGHT
    A5SLIM_PORTRAIT_HEIGHT = A5SLIM_LANDSCAPE_WIDTH

    A6SLIM_LANDSCAPE_WIDTH = 105
    A6SLIM_LANDSCAPE_HEIGHT = 49
    A6SLIM_PORTRAIT_WIDTH = A6SLIM_LANDSCAPE_HEIGHT
    A6SLIM_PORTRAIT_HEIGHT = A6SLIM_LANDSCAPE_WIDTH

    M5_LANDSCAPE_WIDTH = 105
    M5_LANDSCAPE_HEIGHT = 62
    M5_PORTLAIT_WIDTH = M5_LANDSCAPE_HEIGHT
    M5_PORTLAIT_HEIGHT = M5_LANDSCAPE_WIDTH

    # 印刷対象のサイズ
    BASE_PAGE_WIDTH = A4_LANDSCAPE_WIDTH
    BASE_PAGE_HEIGHT = A4_LANDSCAPE_HEIGHT
    # 切り出す1枚のサイズ
    TARGET_PAGE_WIDTH = M5_PORTLAIT_WIDTH
    TARGET_PAGE_HEIGHT = M5_PORTLAIT_HEIGHT

    FIRST_DOT_INTERVAL = 1.25
    FIRST_DOT_SIZE = 0.075
    SECOND_DOT_INTERVAL = 5
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
            # その他追加色
            (colors.HexColor("#451722"), "_阪急マルーン"),
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
        self.pdf_file.setTitle(self.TITLE)
        self.pdf_file.setSubject(self.TITLE)
        self.pdf_file.setPageSize(
            (self.BASE_PAGE_WIDTH*mm, self.BASE_PAGE_HEIGHT*mm))

    def set_color(self, color):
        if self.pdf_file is None:
            raise ValueError('pdf_file is not assigned')

        self.pdf_file.setStrokeColor(color)
        self.pdf_file.setFillColor(color)

    def get_margin(self,
                   pagewidth: int, pageheight: int
                   ) -> Margin:
        # 余白
        width_margin = (self.BASE_PAGE_WIDTH %
                        pagewidth) / 2
        height_margin = (self.BASE_PAGE_HEIGHT %
                         pageheight) / 2
        return Margin(width=width_margin, height=height_margin)

    def draw_split_line(self, color,
                        pagewidth: int, pageheight: int,
                        margin: Margin) -> None:
        if self.pdf_file is None:
            raise ValueError('pdf_file is not assigned')

        self.pdf_file.setStrokeColor(color)
        self.pdf_file.setLineWidth(0.01*mm)

        # 左縦線
        left = (0 + margin.width)
        self.pdf_file.line(
            left * mm,
            0 * mm,
            left * mm,
            self.BASE_PAGE_HEIGHT * mm
        )
        # 右縦線
        right = (self.BASE_PAGE_WIDTH - margin.width)
        self.pdf_file.line(
            right * mm,
            0 * mm,
            right * mm,
            self.BASE_PAGE_HEIGHT * mm
        )
        # 下横線
        bottom = (0 + margin.height)
        self.pdf_file.line(
            0 * mm,
            bottom * mm,
            self.BASE_PAGE_WIDTH * mm,
            bottom * mm
        )
        # 上横線
        top = (self.BASE_PAGE_HEIGHT - margin.height)
        self.pdf_file.line(
            0 * mm,
            top * mm,
            self.BASE_PAGE_WIDTH * mm,
            top * mm
        )

        # A5縦の位置にラインを入れる
        for x in [(
            (x+1) * pagewidth) + margin.width
            for x in range(
            math.floor(self.BASE_PAGE_WIDTH
                       / pagewidth)-1
        )]:
            self.pdf_file.line(
                x * mm,
                0 * mm,
                x * mm,
                self.BASE_PAGE_HEIGHT * mm
            )

        # A5 slimサイズ(148x70)の横線を入れる
        for y in [(
            (y+1) * pageheight) + margin.height
            for y in range(
            math.floor(
                self.BASE_PAGE_HEIGHT
                / pageheight) - 1
        )]:
            self.pdf_file.line(
                0,
                y * mm,
                self.BASE_PAGE_WIDTH * mm,
                y * mm
            )

    def draw_dotgrid(self,
                     color,
                     margin: Margin,
                     interval: float,
                     dotsize: float,
                     pagewidth: int,
                     pageheight: int,
                     offset: float = 0
                     ):
        if self.pdf_file is None:
            raise ValueError('pdf_file is not assigned')

        # 描画前にドットの座標を計算
        points = [((x) * interval + offset + margin.width,
                   (y) * interval + offset + margin.height)
                  for x in range(
            math.floor((pagewidth - offset)
                       / interval) + 1)
                  for y in range(
            math.floor((pageheight - offset)
                       / interval) + 1)
                  ]

        # ページ数
        pageindex = [
            (page_x, page_y)
            for page_x in range(
                math.floor(self.BASE_PAGE_WIDTH / pagewidth))
            for page_y in range(
                math.floor(self.BASE_PAGE_HEIGHT / pageheight))
        ]

        for page_x, page_y in pageindex:
            self.pdf_file.setFillColor(color)
            for x, y in points:
                self.pdf_file.circle(
                    (x + pagewidth * page_x) * mm,
                    (y + pageheight * page_y) * mm,
                    dotsize * mm, stroke=0, fill=1)

    def write_pdf_file(self, color_name: str) -> None:
        if self.pdf_file is None:
            raise ValueError('pdf_file is not assigned')
        self.pdf_file.restoreState()
        self.pdf_file.save()
        print("Save:{0}".format(color_name))

    def create_format(self, color,
                      color_name: str,
                      pagewidth: int, pageheight: int) -> None:
        out_path = self.create_out_path(color_name)
        self.pdf_file = canvas.Canvas(out_path)
        self.pdf_file.saveState()
        self.set_property()
        margin: Margin = self.get_margin(pagewidth, pageheight)
        self.draw_split_line(
            color, pagewidth, pageheight, margin
        )

        self.draw_dotgrid(
            color, margin,
            self.FIRST_DOT_INTERVAL,
            self.FIRST_DOT_SIZE,
            pagewidth,
            pageheight
        )

        self.draw_dotgrid(
            color, margin,
            self.SECOND_DOT_INTERVAL,
            self.SECOND_DOT_SIZE,
            pagewidth,
            pageheight,
            self.FIRST_DOT_INTERVAL * 2
        )
        self.write_pdf_file(color_name)

    def create_format_all_color(self) -> None:
        for color, color_name in self.color_list:
            self.create_format(
                color,
                color_name,
                self.TARGET_PAGE_WIDTH,
                self.TARGET_PAGE_HEIGHT
            )


if __name__ == "__main__":
    format = BaseNoteFormat(BaseNoteFormat.DIRNAME)
    single_color = colors.HexColor("#84B5CF")
    single_color_name = "_白群（びゃくぐん）"
    # format.create_format(single_color, single_color_name, format.TARGET_PAGE_WIDTH, format.TARGET_PAGE_HEIGHT)
    format.create_format_all_color()
