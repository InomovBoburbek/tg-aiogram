import asyncio
import logging
import sys
import json
from aiogram import Bot, Dispatcher, html, F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton

TOKEN = "7931976481:AAEvBr6C1geXIPEd5kK1-eEUnycUFZ-nydI"

dp = Dispatcher()



@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Salom, {html.bold(message.from_user.full_name)}!")
    await message.answer("Ismingizni kiriting!")


@dp.message(Command("help"))
async def command_help(message: Message) -> None:
    markup = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Admin🧑🏻‍💻"), KeyboardButton(text="phone number")],
            [KeyboardButton(text="Owner")]
        ],
        resize_keyboard=True,
        one_time_keyboard=False
    )

    await message.answer("Quyidagi tugmalardan birini tanlang:", reply_markup=markup)


@dp.message(F.text.lower() == "admin🧑🏻‍💻")
async def command_admin(message: Message) -> None:
    await message.answer("@Inomovv_2")


@dp.message(F.text.lower() == "owner")
async def command_owner(message: Message) -> None:
    await message.answer("@martin_0_001")


@dp.message(F.text.lower() == "phone number")
async def command_phone(message: Message) -> None:
    await message.answer("+998 99 807 11 34")


@dp.message(Command("about"))
async def command_about(message: Message) -> None:
    await message.answer("Bu bot siz yozgan so'zni yoki gapni to'tiga o'xshab qaytaradi!")


@dp.message(F.text)
async def echo_handler(message: Message) -> None:
    if message.text.isdigit():
        with open("users.json", "r") as file:
            users = json.load(file)
        if message.text in users:
            user = users[message.text]
            answer = f"Ismi : {user['name']}, yoshi : {user['age']}"
            await message.answer(answer)
        else:
            await message.answer(f"{message.text} id li user yo'q")

async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
