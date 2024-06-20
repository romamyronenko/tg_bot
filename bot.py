import asyncio
import logging
import sys
from os import getenv

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message

from bull_and_cows import generate_random_number, get_bulls_and_cows

TOKEN = getenv("BOT_TOKEN")

dp = Dispatcher()

WORD_LENGTH = 5
WORD = ""


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    global WORD
    WORD = generate_random_number(WORD_LENGTH)

    await message.answer(f"Число згенеровано! Довжина - {WORD_LENGTH} символів")


@dp.message()
async def echo_handler(message: Message) -> None:
    user_word = message.text
    try:
        bulls_and_cows = get_bulls_and_cows(WORD, user_word)
        await message.answer(
            f"Биків: {bulls_and_cows['bulls']}\nКорів: {bulls_and_cows['cows']}"
        )
    except ValueError:
        await message.answer(
            f"Ви ввели рядок довжиною {len(user_word)}, потрібно ввести рядок довжиною {WORD_LENGTH}"
        )


async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
