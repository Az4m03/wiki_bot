import logging
import wikipedia

from aiogram import Bot, Dispatcher, executor, types

import settings

wikipedia.set_lang('ru')

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=settings.API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Добро пожаловать в Bot википедии!")



@dp.message_handler()
async def send_wiki(message: types.Message):
    try:
        respond = wikipedia.summary(message.text)
        await message.answer(respond)
    except:
        await message.answer('Информация не найдено')




if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)