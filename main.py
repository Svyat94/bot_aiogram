from aiogram import Bot, Dispatcher, types, executor
from aiogram.types.web_app_info import WebAppInfo


bot = Bot('your_id_token') # Токен телеграм бота
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    markup = types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton('Открыть веб страницу', web_app=WebAppInfo(url='https://github.com/Svyat94')))
    await message.answer('Привет, это моя страница в GitHub, подпишись 😊!', reply_markup=markup)

executor.start_polling(dp)