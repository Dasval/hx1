from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.web_app_info import WebAppInfo

bot = Bot('6735704124:AAFqv0KtyFg6T7i2W9779FOIHX6L-s1rFLA')
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    markup = types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton('Suda', web_app=WebAppInfo(url='https://dasval.github.io/10.github.io/')))
    await message.answer('Привет!', reply_markup=markup)





executor.start_polling(dp)