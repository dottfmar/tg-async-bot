import asyncio
import os

from aiogram import Bot, Dispatcher, types, Router
from aiogram.filters import CommandStart
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import random

from dotenv import load_dotenv

load_dotenv()

API_TOKEN = os.getenv("API_TOKEN")

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

quotes = [
    "Не чекай ідеального моменту. Бери момент і роби його ідеальним.",
    "Секрет зміни — зосередитися не на боротьбі зі старим, а на створенні нового.",
    "Ти здатен на більше, ніж думаєш.",
    "Великі досягнення починаються з малих кроків.",
]

creative_ideas = [
    "Намалюй картину, де головний герой — приручений дракон, що живе в сучасному місті.",
    "Напиши вірш про перший дощ після літа.",
    "Спробуй зробити фото з незвичайної перспективи — знизу вверх або через воду.",
    "Придумай історію про вигадану планету.",
]

riddles = [
    "Що завжди попереду, але ніколи не видно?",
    "Я маю коріння, але не можу рости. Що я?",
    "Що не можна тримати в руках, навіть якщо це дуже хочеться?",
]

facts = [
    "Більшість пилу у твоєму домі — це частинки шкіри твоїх домашніх тварин та людей.",
    "Коли ми сміємося, наше тіло виробляє ендорфіни, що покращують настрій.",
    "Картопля була першим овочем, який відправили в космос.",
    "Найбільша зірка, яку ми знаємо, має діаметр у понад 1700 разів більший за Сонце.",
]


@router.message(CommandStart())
async def send_welcome(message: types.Message):
    await message.reply(
        "Привіт! Я твій надихаючий бот! Натисни на одну з кнопок і отримаєш щось цікаве!",
        reply_markup=keyboard,
    )


@router.message(lambda message: message.text == "Мотиваційна цитата")
async def send_quote(message: types.Message):
    quote = random.choice(quotes)
    await message.reply(quote, reply_markup=keyboard)


@router.message(lambda message: message.text == "Ідея для творчості")
async def send_creative_idea(message: types.Message):
    idea = random.choice(creative_ideas)
    await message.reply(idea, reply_markup=keyboard)


@router.message(lambda message: message.text == "Загадка")
async def send_riddle(message: types.Message):
    riddle = random.choice(riddles)
    await message.reply(riddle, reply_markup=keyboard)


@router.message(lambda message: message.text == "Цікаві факти")
async def send_fact(message: types.Message):
    fact = random.choice(facts)
    await message.reply(fact, reply_markup=keyboard)


async def start_chat():
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(start_chat())
