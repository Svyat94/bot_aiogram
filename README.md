#### Bot на aiogram 2.23.1
---
## Создаем бота в телеграм 
1. Находим в поиске [bot_father](https://t.me/BotFather)https://t.me/BotFather
2. Выполняем команду /star потом /newbot
3. Выбираем имя
4. Находим токен нашего бота выполняем команду /mybots выбираем своего бота и нажимаем API Token
---
## Скачиваем репозиторий 
Выполняем команду в терминале git clone https://github.com/Svyat94/my_project.git
#Создаем виртуальное окружение 
в терминале вводим 
py -m venv venv
. venv/Scripts/activate
pip install aiogram==2.23.1
или через requirements.txt: 
pip install -r requirements.txt
---
## Запускаем бота 
Меняем строчку в кавычках вместо 'your_id_token' указываем токен, который нам дал bot_father
bot = Bot('your_id_token') # Токен вашего телеграм бота
