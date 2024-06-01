[![Static Badge](https://img.shields.io/badge/Telegram-Channel-Link?style=for-the-badge&logo=Telegram&logoColor=white&logoSize=auto&color=blue)](https://t.me/hidden_coding)

[![Static Badge](https://img.shields.io/badge/Telegram-Chat-yes?style=for-the-badge&logo=Telegram&logoColor=white&logoSize=auto&color=blue)](https://t.me/hidden_codding_chat)

[![Static Badge](https://img.shields.io/badge/Telegram-Bot%20Link-Link?style=for-the-badge&logo=Telegram&logoColor=white&logoSize=auto&color=blue)](https://t.me/cexio_tap_bot%3Fstart%3D1717162889191233)

<img src="https://github.com/AlexKrutoy/CEX.IO-bot/assets/65369825/63571e45-9fc3-4982-9156-7a88f9906bc4" width="750" height="525"/>

<img src="https://github.com/AlexKrutoy/CEX.IO-bot/assets/65369825/3d216564-546d-46c8-bf25-d1fbf50dd0fd" width="600" height="700"/>

## Рекомендация перед использованием

# 🔥🔥 Используйте PYTHON 3.10 🔥🔥

> 🇪🇳 README in english available [here](README.md)

## Функционал  
| Функционал                                                     | Поддерживается  |
|----------------------------------------------------------------|:----------------:|
| Многопоточность                                                |        ✅        |
| Привязка прокси к сессии                                       |        ✅        |
| Авто-Клик монеты                                               |        ✅        |
| Авто-Старт фермы                                               |        ✅        |
| Определенное количество кликов                                 |        ✅        |
| Авто-Забирание наград за сквад                                 |        ✅        |
| Авто-Выполнение задач                                          |        ✅        |
| Поддержка tdata / pyrogram .session / telethon .session        |        ✅        |


## [Настройки](https://github.com/404)
| Настройка                | Описание                                                                                    |
|--------------------------|:---------------------------------------------------------------------------------------------:|
| **API_ID / API_HASH**    | Данные платформы, с которой запускать сессию Telegram (сток - Android)                      |
| **FARM_MINING_ERA**      | Нужно ли автоматическии запускать ферму (напр. True)                                        |                                
| **TAPS**                 | Нужен ли авто-клик монетки (напр. True)                                                     |
| **TAPS_AMOUNT**          | Сколько тапов будет кликнуто (напр. [100, 1000])                                            |
|**CLAIM_SQUAD_REWARD**    | Авто-Забирание наград за сквад (напр. True)                                                 |
|**CLAIM_TASKS**           | Авто-выполнение заданий (единожды) ((напр. True))                                           |
| **USE_PROXY_FROM_FILE**  | Использовать-ли прокси из файла `bot/config/proxies.txt` (True / False)                     |

## Быстрый старт 📚
1. Чтобы установить библиотеки в Windows, запустите INSTALL.bat.
2. Для запуска бота используйте `START.bat` (или в консоли: `python main.py`).

## Предварительные условия
Прежде чем начать, убедитесь, что у вас установлено следующее:
- [Python](https://www.python.org/downloads/) **версии 3.10**

## Получение API ключей
1. Перейдите на сайт [my.telegram.org](https://my.telegram.org) и войдите в систему, используя свой номер телефона.
2. Выберите **"API development tools"** и заполните форму для регистрации нового приложения.
3. Запишите `API_ID` и `API_HASH` в файле `.env`, предоставленные после регистрации вашего приложения.

## Установка
Вы можете скачать [**Репозиторий**](https://github.com/AlexKrutoy/CEX.IO-bot) клонированием на вашу систему и установкой необходимых зависимостей:
```shell
git clone https://github.com/AlexKrutoy/CEX.IO-bot.git
cd CEX.IO-bot
```

# Linux
```shell
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
cp .env-example .env
nano .env  # Здесь вы обязательно должны указать ваши API_ID и API_HASH , остальное берется по умолчанию
python3 main.py
```

# Windows
```shell
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
copy .env-example .env
# Указываете ваши API_ID и API_HASH, остальное берется по умолчанию
python main.py
```

Также для быстрого запуска вы можете использовать аргументы, например:
```shell
~/CEX.IO-bot >>> python3 main.py --action (1/2)
# Или
~/CEX.IO-bot >>> python3 main.py -a (1/2)

# 1 - Запускает кликер
# 2 - Создает сессию
```




### Контакты

Для поддержки или вопросов, свяжитесь со мной в Telegram: [@UNKNXWNPLXYA](https://t.me/UNKNXWNPLXYA)
