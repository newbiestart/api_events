import random
import asyncio
import os
import sys

from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from asgiref.sync import sync_to_async

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
import django
django.setup()

from users.models import User

BOT_TOKEN = "BU_YERGA_BOT_TOKEN"
LOGIN_URL = "http://127.0.0.1:8000/api/token/"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

phone_keyboard = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text="📞 Telefon raqam yuborish", request_contact=True)]],
    resize_keyboard=True
)

def generate_password():
    return str(random.randint(10000000, 99999999))

@dp.message(CommandStart())
async def start_handler(message: types.Message):
    await message.answer(
        "📞 Telefon raqamingizni yuboring:",
        reply_markup=phone_keyboard
    )

@dp.message(lambda msg: msg.contact is not None)
async def contact_handler(message: types.Message):
    phone = message.contact.phone_number
    telegram_id = message.from_user.id

    user = await sync_to_async(User.objects.filter(phone=phone).first)()

    password = generate_password()

    if not user:
        user = await sync_to_async(User.objects.create_user)(
            phone=phone,
            full_name=message.from_user.full_name or "Telegram user",
            password=password
        )
        user.telegram_id = telegram_id
        await sync_to_async(user.save)()

        await message.answer(
            "🆕 Siz avtomatik ro‘yxatdan o‘tkazildingiz!"
        )

    else:
        user.telegram_id = telegram_id
        user.set_password(password)
        await sync_to_async(user.save)()

    await message.answer(
        f"🔑 Yangi parolingiz:\n\n"
        f"`{password}`\n\n"
        f"🌐 Login: {LOGIN_URL}",
        parse_mode="Markdown",
        reply_markup=types.ReplyKeyboardRemove()
    )

async def main():
    print("🤖 Bot ishlayapti...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
