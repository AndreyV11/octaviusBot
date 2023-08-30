from aiogram import Bot, Dispatcher, executor, types
from config import TOKEN_API, HELP_INFO, DESCRIPTION_INFO, HELLO_USER

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)


async def on_startup(_):
    print("Бот был успешно запущен")


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer(text="<em>Добро пожаловать на наш Телеграмм-канал!</em>", parse_mode="HTML")
    await message.delete()


@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await message.answer(text=HELP_INFO)


@dp.message_handler(commands=['description'])
async def description_command(message: types.Message):
    await message.answer(text=DESCRIPTION_INFO)


@dp.message_handler()
async def hello_echo_command(message: types.Message):
    if message.text.lower() in HELLO_USER:
        await message.answer(text=message.text)
    if message.text.lower() in ["спасибо", "thanks, thank you"]:
        await message.reply(text="❤️")
        await bot.send_sticker(message.from_user.id,
                               sticker="CAACAgIAAxkBAAEKLEZk73F90AhWbUEQFibnOaw98AmziwACQAEAAooSqg6FLrYwmvbwXzAE")
    if message.text == "🐙":
        await message.reply(text="❤️")


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)
