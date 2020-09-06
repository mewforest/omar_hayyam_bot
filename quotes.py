"""
Скрипт, генерирующий цитаты из текста
"""
import logging
from PIL import Image, ImageDraw, ImageFont
import textwrap

""" Путь к файлу шрифта """
FONT_PATH = 'fonts/marta/Marta_Italic.otf'
""" Размер шрифта """
FONT_SIZE = 65
""" Путь к изображению для фона """
IMG_BACKGROUND = 'images/quote_bg.jpg'


def generate_quote(text: str) -> Image:
    """
    Рисует текст на изображении.

    Вначале инициализируются базовые переменные:
    - изображение (im)
    - объект для рисования (draw)
    - ширина и высота изображения (w, h)
    - отступ между строками текста (padding)
    - список строк с шириной 20 символов (text_lines)
    - шрифт для текста (font)
    - стартовая высота (current_height)

    Далее перебираются строки и, для каждой строки текста происходит следующее:
    - Высчитывается ширина текущей строки с помощью draw.textsize()
    - Строка отрисовывается на изображении со следующими параметрами:
    -- отступ слева - чтобы текст был ровно посередине, он должен быть равен (w - w_text) / 2, однако, в данном случае,
       чтобы текст не наезжал на портрет, текст дополнительно сдвигается на 150 пикселей вправо
    -- отступ сверху равен текущей высоте (current_height)
    -- цвет текста (fill) равен rgb(193, 99, 55) или #C16337
    -- текст строки и шрифт
    - Отступ сверху (current_height) увеличивается для того, чтобы следующая строка не наезжала предыдущую

    :param text: str - текст для изображения цитаты
    :return: PIL.Image - объект изображения
    """
    im = Image.open(IMG_BACKGROUND)
    draw = ImageDraw.Draw(im)
    w, h = im.size
    padding = FONT_SIZE + 5
    text_lines = textwrap.wrap(text, width=20)
    font = ImageFont.truetype(FONT_PATH, FONT_SIZE)
    current_height = h / 3
    for line in text_lines:
        w_text, h_text = draw.textsize(line, font=font)
        draw.text(
            ((w - w_text) / 2 + 150, current_height),
            line,
            fill=(193, 99, 55),
            font=font,
        )
        current_height += padding
    return im


if __name__ == '__main__':
    """ Код для проверки работы модуля """
    logging.basicConfig(level=logging.INFO)
    image = generate_quote(text=input('Введите текст > '))
    image.save('images/quote_text.jpg', quality=30)
    logging.info('Успех! Результат сохранился в images/quote_text.jpg')
