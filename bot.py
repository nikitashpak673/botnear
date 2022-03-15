from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher,FSMContext
from aiogram.utils import executor
from settings import TOKEN
from parser2 import parse
from time import sleep
from aiogram.dispatcher.filters import Text
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import StatesGroup,State
bot = Bot(token=TOKEN)
storage1=MemoryStorage()
dp = Dispatcher(bot,storage=storage1)
class register(StatesGroup):
    register1=State()
    register2=State()
@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Отслеживать курс", "Узнать текущий курс"]
    keyboard.add(*buttons)
    await message.answer("Привет!\nЯ бот для проверки курса nearcoin!\nЧто вы хотите сделать?\n",reply_markup=keyboard)
@dp.message_handler(Text(equals="Отслеживать курс"))
async def process_foloow_cource(msg: types.Message):
    await bot.send_message(msg.from_user.id, "Введите значение желаемого курса, при котором бот отправит уведомление")
    await register.register1.set()
@dp.message_handler(state=register.register1)
async def enter_value(msg:types.Message,state:FSMContext):
    value=msg.text
    await state.update_data(register1=value)
    await bot.send_message(msg.from_user.id,f"Бот начал отслеживать по заданному курсу:{value}$")
    try:
        value=float(msg.text)
        course = parse(value2=value)
        await bot.send_message(msg.from_user.id,f"Значение принято , текущий курс {course[1]}")
        while(True):
            if(parse(value2=value)[0]>=value):
                await bot.send_message(msg.from_user.id,f"""Выводи по курсу {course[0]}""")
                sleep(30)
            else:
                sleep(3600)

    except Exception as ex:
        print(ex)
        await bot.send_message(msg.from_user.id,"Ошибка ввода,введите число")




@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply("Напиши мне что-нибудь, и я отпрпавлю этот текст тебе в ответ!")







if __name__ == '__main__':
    executor.start_polling(dp)