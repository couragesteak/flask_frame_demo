import random, string
from io import BytesIO
from PIL import ImageFont, ImageDraw, Image


class ImageCode:
    # 生成用于绘制字符串的随机颜色
    def rand_color(self):
        red = random.randint(32, 200)
        green = random.randint(22, 255)
        blue = random.randint(0, 200)
        return red, green, blue

    # 生成4位随机字符串
    def get_text(self):
        # sample 用于从一个大的列表或字符串中，随机取得N个字符，来构建一个子列表
        list = random.sample(string.ascii_letters + string.digits, 4)
        return ''.join(list)

    # 画一些干扰线，其中draw为PIL中的ImageDraw对象
    def draw_lines(self, draw, num, width, height):
        for num in range(num):
            x1 = random.randint(0, width / 2)
            y1 = random.randint(0, height / 2)
            x2 = random.randint(0, width / 2)
            y2 = random.randint(height / 2, height)
            draw.line(((x1, y1), (x2, y2)), fill='black', width=2)

    # 绘制验证码图片
    def draw_verify_code(self):
        code = self.get_text()
        # 设定图片大小，可根据实际需求调整
        width, height = 120, 50
        # 创建图片对象，并设定背景为白色
        im = Image.new('RGB', (width, height), 'white')
        # 选择使用何种字体大小
        font = ImageFont.truetype(font='/usr/local/web/font/arial.ttf', size=40)
        draw = ImageDraw.Draw(im)
        # 绘制字符串
        for i in range(4):
            draw.text((5 + random.randint(-3, 3) + 23 * i, 5 + random.randint(-3, 3)),
                      text=code[i], fill=self.rand_color(), font=font)
        # 绘制干扰线
        self.draw_lines(draw, 4, width, height)

        # im.show()
        return im, code

    # 生成图片验证码并返回控制器
    def get_code(self):
        image, code = self.draw_verify_code()
        buf = BytesIO()
        image.save(buf, 'jpeg')
        bstring = buf.getvalue()  # 通过字节码获取
        return code, bstring
