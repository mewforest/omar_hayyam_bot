# Омар Хайям вещает...

Чат-бот для Telegram, имитирующий цитаты Омар Хайяма.

[@omar_hayyam_bot](http://t.me/omar_hayyam_bot)

Основная задача бота - веселить пользователей 🙂

Основная задача данного репозитория - показать, как устроен бот
с функционалом по обработке изображений, выдерживающий высокую нагрузку.

## Пример диалога с ботом

![screenshot](https://github.com/mewforest/omar_hayyam_bot/blob/master/preview.png?raw=true)

## Установка и запуск

Чтобы скачать исходный код, воспользуйтесь
[постоянной ссылкой](https://github.com/mewforest/omar_hayyam_bot/archive/master.zip)
или склонируйте проект с помощью [git](https://git-scm.com/downloads):
```bash
git clone https://github.com/mewforest/omar_hayyam_bot.git
```
### Windows 
Для того, чтобы запустить бот локально у вас на устройстве,
установите [Python 3.8](https://www.python.org/downloads/) (во время
установки не пропустите галочку у пункта `Add Python 3.X to PATH`).

Выполните установку всех необходимых библиотек и запустите бот:
```bash
python -m pip install -r -u requirements.txt
python bot.py
```

### Linux

Для Linux можно будет выполнить все шаги через терминал (_bash_):
```bash
sudo apt update && apt install python3-pip python-imaging
python3 -m pip install -r -u requirements.txt
python3 bot.py
```

## Обратная связь
Если вы нашли ошибку в коде или хотите предложить улучшения в коде,
отправляйте свои варианты через
[pull requests](https://github.com/mewforest/omar_hayyam_bot/pulls).

По всем вопросам и предложениям к боту используйте раздел
[issues](https://github.com/mewforest/omar_hayyam_bot/issues).

## Лицензия

TL;DR: Свободная к распространению лицензия с сохранением
ссылок на оригинальный репозиторий.

This project is licensed under the Apache License, 
see the [LICENSE](https://github.com/mewforest/omar_hayyam_bot/blob/master/LICENSE)
file for details.
