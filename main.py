from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton

with open("token.txt") as token_bot:
    token_id = token_bot.read()
bot = Bot(token_id)
dp = Dispatcher(bot)

button1 = KeyboardButton("choose Catgegory")
button2 = KeyboardButton("Button2")
keyboard1 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(button1).add(button2)

button3 = KeyboardButton("#שונות")
button4 = KeyboardButton("#קניות")
button5 = KeyboardButton("#חשבונות")
button6 = KeyboardButton("#חשמל")
button7 = KeyboardButton("#אוכל_בחוץ")
keyboard2 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(button3).add(button4).add(button5).add(button6).add(button7)



@dp.message_handler(commands=['start', 'help'])
async def welcome(message: types.Message):
    await message.reply("Hello I am the Bot", reply_markup=keyboard1)


@dp.message_handler()
async def kb_answer(message: types.Message):
    if message.text == 'choose Catgegory':
        await message.answer('hey How Are you?')
        await message.answer("choose",reply_markup=keyboard2)
    elif message.text == "Button2":
        await message.answer("This is reply num 2")
    else:
        await message.answer(f"Your Message Has Received {message.text}")

async def second_page(message: types.Message):
    await message.reply("choose Category", reply_markup=keyboard2)

executor.start_polling(dp)
