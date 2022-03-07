from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from settings import TOKEN
from botnear.parser2 import parse

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.answer("Привет!\nЯ бот для проверки курса nearcoin!\nВведите желаемый курс, при котором я отправлю уведомление\nПример ввода 11.23")


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply("Напиши мне что-нибудь, и я отпрпавлю этот текст тебе в ответ!")


@dp.message_handler()
async def echo_message(msg: types.Message):
    try:
        value=float(msg.text)
        while(True):
            if(parse(value2=value)>=value):
                await bot.send_message(msg.from_user.id,f"""Выводи по курсу {parse(value2=value)}""")
    except:
        await bot.send_message(msg.from_user.id,"Ошибка ввода,введите число")




if __name__ == '__main__':
    executor.start_polling(dp)