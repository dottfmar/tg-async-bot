import asyncio
import os
from aiogram import Bot, Dispatcher, types, Router
from aiogram.filters import CommandStart
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from google import genai
from dotenv import load_dotenv

load_dotenv()

API_TOKEN = os.getenv("API_TOKEN")
GENAI_API_KEY = os.getenv("GENAI_API_KEY")

bot = Bot(token=API_TOKEN)
dp = Dispatcher()
router = Router()

keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Мотиваційна цитата"),
            KeyboardButton(text="Ідея для творчості"),
        ],
        [KeyboardButton(text="Загадка"), KeyboardButton(text="Цікаві факти")],
    ],
    resize_keyboard=True,
)


async def get_generated_quote():
    client = genai.Client(api_key=GENAI_API_KEY)
    response = client.models.generate_content(
        model="gemini-2.0-flash", contents=["Мотиваційна цитата"]
    )
    return response.text.strip()


async def get_generated_creative_idea():
    client = genai.Client(api_key=GENAI_API_KEY)
    response = client.models.generate_content(
        model="gemini-2.0-flash", contents=["Ідея для творчості"]
    )
    return response.text.strip()


async def get_generated_riddle():
    client = genai.Client(api_key=GENAI_API_KEY)
    response = client.models.generate_content(
        model="gemini-2.0-flash", contents=["Загадка"]
    )
    return response.text.strip()


async def get_generated_fact():
    client = genai.Client(api_key=GENAI_API_KEY)
    response = client.models.generate_content(
        model="gemini-2.0-flash", contents=["Цікавий факт"]
    )
    return response.text.strip()


@router.message(CommandStart())
async def send_welcome(message: types.Message):
    await message.reply(
        "Привіт! Я твій надихаючий бот! Натисни на одну з кнопок і отримаєш щось цікаве!",
        reply_markup=keyboard,
    )


@router.message(lambda message: message.text == "Мотиваційна цитата")
async def send_quote(message: types.Message):
    quote = await get_generated_quote()
    await message.reply(quote, reply_markup=keyboard)


@router.message(lambda message: message.text == "Ідея для творчості")
async def send_creative_idea(message: types.Message):
    idea = await get_generated_creative_idea()
    await message.reply(idea, reply_markup=keyboard)


@router.message(lambda message: message.text == "Загадка")
async def send_riddle(message: types.Message):
    riddle = await get_generated_riddle()
    await message.reply(riddle, reply_markup=keyboard)


@router.message(lambda message: message.text == "Цікаві факти")
async def send_fact(message: types.Message):
    fact = await get_generated_fact()
    await message.reply(fact, reply_markup=keyboard)


async def start_chat():
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(start_chat())
