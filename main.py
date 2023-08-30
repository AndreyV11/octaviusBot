from aiogram import Bot, Dispatcher, executor, types
from config import TOKEN_API, HELP_INFO, DESCRIPTION_INFO, HELLO_USER

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)


async def on_startup(_):
    print("Бот был успешно запущен")


# функция приветствия, отправка стикера, message.from_user.id -> отправляет сообщение в чат пользователю
@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer(text="<em>Добро пожаловать на наш Телеграмм-канал!</em>", parse_mode="HTML")
    await bot.send_sticker(message.from_user.id,
                           sticker="CAACAgIAAxkBAAEKLEpk73VCGsVsdN5T3S_FqvBtg6PSpwACtgkAAnlc4gnGTnKNypclSDAE")
    await message.delete()


# функция help, список команд, parse_mode - разметка сообщения
@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await bot.send_message(text=HELP_INFO, parse_mode="HTML",
                           chat_id=message.from_user.id)
    await message.delete()


# описание бота, message.answer отвечает туда, откуда пришло сообщение
@dp.message_handler(commands=['description'])
async def description_command(message: types.Message):
    await message.answer(text=DESCRIPTION_INFO)


# отправка изображения, доступно как по интернет-ссылке, так и из локальной памяти, message.chat.id - в групповой чат
@dp.message_handler(commands=["photo"])
async def photo_command(message: types.Message):
    await bot.send_photo(chat_id=message.chat.id,
                         photo="https://i.pinimg.com/originals/1e/b3/78/1eb3786697979899fadbd770f05ba9d5.png")
    await message.delete()


# отправка сообщений в зависимомти от сообщения пользователя
@dp.message_handler()
async def hello_echo_command(message: types.Message):
    if message.text.lower() in HELLO_USER:
        await message.answer(text=message.text)
    if message.text.lower() in ["спасибо", "thanks, thank you"]:
        await message.reply(text="❤️")
        await bot.send_sticker(message.chat.id,
                               sticker="CAACAgIAAxkBAAEKLEZk73F90AhWbUEQFibnOaw98AmziwACQAEAAooSqg6FLrYwmvbwXzAE")
    if message.text == "🐙":
        await message.reply(text="❤️")


## отправка геолокации
#@dp.message_handler(commands=["location"])
#async def location_command(message: types.Message):
#    await bot.send_location(chat_id=message.from_user.id, longitude=55, latitude=18)
#    await message.delete()


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)
    # skip_updates=True -> бот не будет отвечать на сообщения, полученные оффлайн
    # on_startup - функция, вызывающаяся при запуске бота
