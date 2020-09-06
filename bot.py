"""
Чат-бот для Telegram, имитирующий цитаты Омар Хайяма.

Омар Хайям вещает...
@omar_hayyam_bot
http://t.me/omar_hayyam_bot

"""
import asyncio
import logging
import os
import sys
import io
from functools import partial
from PIL.Image import Image
from aiogram import Bot, Dispatcher, executor, types
from concurrent.futures.thread import ThreadPoolExecutor
"""
Импорт файла generate_quote.py из той же папки происходит с помощью добавления текущей папки в переменную среды PATH.
Это позволяет производить абсолютный импорт, вместо относительного, который не будет работать, поскольку код бота не 
оформлен в виде модуля. PyCharm/VSCode могут не понимать этот хак, поэтому для них производится относительный импорт.
"""
sys.path.append(os.path.dirname(__file__))
try:
    from quotes import generate_quote
except ImportError:
    from .quotes import generate_quote


"""
Установите свой ключ от бота (получить его можно у @BotFather) в переменную среды TG_API_KEY или вставьте его сюда
вручную (не рекомендуется). 
"""
API_TOKEN = os.getenv('TG_API_KEY') or '1234567890'
""" Максимальное количество символов для текста """
MAX_CHARACTERS = 70
""" Максимальное количество одновременно генерируемых изображений """
MAX_THREADS = 10

"""
(1) Настраиваем логирование для вывода информационных сообщений
(2) Инициализируем бот
(3) Инициализируем диспетчер бота для обработки запросов
(4) Создаем многопоточную очередь (thread pool) для выполнения в ней синхроннных функций
"""
logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
thread_pool = ThreadPoolExecutor(max_workers=MAX_THREADS)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    """ Обработчик команды /start """
    await message.answer(f'🧙 ‍Ты знаешь меня, как талантливого мыслителя, а я знаю, {message.from_user.full_name}, '
                         f'что ты можешь меня удивить!\n\nПоделись своими умными мыслями скажи что-нибудь мне... '
                         f'Вдруг я этого не говорил? 🤔')


@dp.message_handler()
async def quote(message: types.Message):
    """
    Обработчик всех текстовых сообщений. На каждый присланный текст пользователем, отправляет картинку с цитатой.

    - async_generate_quote() возвращает объект изображения из библиотеки PIL (Pillow)
    - io.BytesIO - это объект файлового потока, буфер, который вместо файловой системы, хранит содержимое в оперативной
      памяти. Без данного объекта пришлось бы сохранять изображение в файлувую систему и заново открывать для отправки
    - Чтобы сохраненное изображение считалось из буфера правильно, необходимо указать, что считывать изображение нужно
      с самого начала: image_io.seek(0)
    - reply_photo() отпраляет ответ пользователю с полученным изображением
    """
    logging.info(f'{message.from_user.full_name} написал(а) "{message.text}"')
    if len(message.text) < MAX_CHARACTERS:
        text = message.text
        image_pil = await async_generate_quote(text)
        image_io = io.BytesIO()
        image_pil.save(image_io, format='JPEG', quality=30)
        image_io.seek(0)
        await message.reply_photo(image_io, caption='Я уже это говорил однажды.. ☝')
    else:
        await message.answer(f'🙅‍♂️Не нужно много слов... Любые слова имеют свой вес. '
                             f'Будь краток, 50 символов достаточно, ведь ровно столько же каплей на листках сакуры 🌸')


async def async_generate_quote(text: str) -> Image:
    """
    Асинхроннаая обёртка, которая отправляет синхронную функцию на выполнение в многопоточную очередь и ждёт результата.

    - get_event_loop() получает цикл событий (поток, котором выполняются асихронные функции - корутины)
    - loop.run_in_executor() позволяет асинхронно выполнить некоторую функцию в исполнителе, которым и является очередь
    - functools.partial() позволяет передать аргументы в функцию, не выполняя её

    :param text: str - текст для синхронной функции generate_quote
    :return: PIL.Image - объект изображения
    """
    loop = asyncio.get_event_loop()
    return await loop.run_in_executor(
        thread_pool,
        partial(generate_quote, text)
    )

if __name__ == '__main__':
    """ Запуск бота """
    executor.start_polling(dp, skip_updates=False)
