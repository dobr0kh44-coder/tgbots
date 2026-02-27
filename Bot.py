from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils import executor
import os

TOKEN = os.getenv("8652356070:AAFSknas3mKkqs4L4R12ITcTRftartdtw4E")

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

rules_button = InlineKeyboardMarkup()
rules_button.add(
    InlineKeyboardButton("📜 Правила", url="https://t.me/dobr0deichat/4379")
)

@dp.message_handler(content_types=["text"])
async def auto_reply(message: types.Message):
    if message.chat.type in ["group", "supergroup"]:
        await message.reply(
            "Приветствую в канале Добродея\n"
            "прежде чем писать в чате ознакомьтесь с правилами",
            reply_markup=rules_button
        )

if __name__ == "__main__":
    executor.start_polling(dp)