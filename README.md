[![Static Badge](https://img.shields.io/badge/Telegram-Channel-Link?style=for-the-badge&logo=Telegram&logoColor=white&logoSize=auto&color=blue)](https://t.me/hidden_coding)

[![Static Badge](https://img.shields.io/badge/Telegram-Chat-yes?style=for-the-badge&logo=Telegram&logoColor=white&logoSize=auto&color=blue)](https://t.me/hidden_codding_chat)

[![Static Badge](https://img.shields.io/badge/Telegram-Bot%20Link-Link?style=for-the-badge&logo=Telegram&logoColor=white&logoSize=auto&color=blue)](https://t.me/cexio_tap_bot%3Fstart%3D1717162889191233)

<img src="https://github.com/AlexKrutoy/CEX.IO-bot/assets/65369825/63571e45-9fc3-4982-9156-7a88f9906bc4" width="750" height="525"/>

<img src="https://github.com/AlexKrutoy/CEX.IO-bot/assets/65369825/3d216564-546d-46c8-bf25-d1fbf50dd0fd" width="600" height="700"/>

## Recommendation before use

# 🔥🔥 Use PYTHON 3.10 🔥🔥

> 🇷 🇺 README in russian available [here](README-RU.md)

## Features  
| Feature                                                     | Supported  |
|---------------------------------------------------------------|:----------------:|
| Multithreading                                                |        ✅        |
| Proxy binding to session                                      |        ✅        |
| Auto-Click coin                                               |        ✅        |
| Auto-Start abd Auto-Claim farm                                |        ✅        |
| Specify number of taps                                        |        ✅        |
| Auto-claim squad reward                                       |        ✅        |
| Auto-start, auto-check and auto-claim tasks                   |        ✅        |
| Auto referral                                                 |        ✅        |
| Support for tdata / pyrogram .session / telethon .session     |        ✅        |


## [Settings](https://github.com/https://github.com/404)
| Settings | Description |
|--------------------------|:---------------------------------------------------------------------------------------------:|
| **API_ID / API_HASH**    | Platform data from which to run the Telegram session (default - android)                     |
| **FARM_MINING_ERA**      | Whether to automatically start the farm (e.g. True)                                          |                                
| **TAPS**                 | Whether to auto-click the coin (e.g. True)                                                   |
| **TAPS_AMOUNT**          | How many taps will be clicked (e.g. [100, 1000])                                             |
| **CLAIM_SQUAD_REWARD**   | Auto claim squad rewards (e.g. True)                                                         |
| **CLAIM_TASKS**          | Auto tasks (one time) ((eg. True))                                                           |
| **REF_ID**               | Argument from referral bot link after ?start={argument}                                      |
| **USE_PROXY_FROM_FILE**  | Whether to use a proxy from the bot/config/proxies.txt file (True / False)                   |

## Quick Start 📚

To install libraries and run bot - open run.bat on Windows

## Prerequisites
Before you begin, make sure you have the following installed:
- [Python](https://www.python.org/downloads/) **version 3.10**

## Obtaining API Keys
1. Go to my.telegram.org and log in using your phone number.
2. Select "API development tools" and fill out the form to register a new application.
3. Record the API_ID and API_HASH provided after registering your application in the .env file.

## Installation
You can download the [**repository**](https://github.com/AlexKrutoy/CEX.IO-bot) by cloning it to your system and installing the necessary dependencies:
```shell
git clone https://github.com/AlexKrutoy/CEX.IO-bot.git
cd CEX.IO-bot
```

Then you can do automatic installation by typing:

Windows:
```shell
run.bat
```

Linux:
```shell
run.sh
```

# Linux manual installation
```shell
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
cp .env-example .env
nano .env  # Here you must specify your API_ID and API_HASH, the rest is taken by default
python3 main.py
```

You can also use arguments for quick start, for example:
```shell
~/CEX.IO-bot >>> python3 main.py --action (1/2)
# Or
~/CEX.IO-bot >>> python3 main.py -a (1/2)

# 1 - Run clicker
# 2 - Creates a session
```

# Windows manual installation
```shell
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
copy .env-example .env
# Here you must specify your API_ID and API_HASH, the rest is taken by default
python main.py
```

You can also use arguments for quick start, for example:
```shell
~/CEX.IO-bot >>> python main.py --action (1/2)
# Or
~/CEX.IO-bot >>> python main.py -a (1/2)

# 1 - Run clicker
# 2 - Creates a session
```




### Contacts

For support or questions, contact me on Telegram: [@UNKNXWNPLXYA](https://t.me/UNKNXWNPLXYA)

