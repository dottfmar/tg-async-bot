# Бот на aiogram

Цей бот створений з використанням бібліотеки `aiogram` для Telegram API. Бот надає кілька інтерактивних функцій, включаючи мотиваційні цитати, ідеї для творчості, загадки та цікаві факти. Бот дозволяє користувачам вибирати з різних кнопок для отримання контенту.

## Використані технології

- **Python** — основна мова програмування для розробки бота.
- **aiogram** — асинхронна бібліотека для роботи з Telegram Bot API.
- **python-dotenv** — бібліотека для завантаження змінних середовища з `.env` файлу.
- **Telegram API** — інтерфейс для взаємодії з Telegram.

## Функціональність бота

1. **Команда `/start`** — при активації цієї команди бот вітає користувача та пропонує вибір з кнопок:
   - **Мотиваційна цитата** — надає випадкову мотиваційну цитату.
   - **Ідея для творчості** — генерує ідеї для творчих завдань.
   - **Загадка** — надає випадкову загадку.
   - **Цікаві факти** — дає випадковий цікавий факт.
   
2. **Вибір кнопок** — користувач може вибирати одну з кнопок для отримання контенту. Кожна кнопка генерує випадковий елемент із відповідного списку:
   - Мотиваційні цитати.
   - Ідеї для творчості.
   - Загадки.
   - Цікаві факти.

3. **Змінні середовища** — токен бота зберігається у `.env` файлі для більшої безпеки та зручності. Використовується бібліотека `python-dotenv` для завантаження змінних середовища.

## Як запустити

### Крок 1: Клонування репозиторію

Клонуйте репозиторій на ваш комп'ютер:

```bash
git clone https://github.com/dottfmar/tg-async-bot.git
cd tg-async-bot
```

### Крок 2: Встановлення залежностей

Встановіть залежності:

```bash
pip install poetry
poetry install
```

### Крок 3: Запуск бота

### Важливо!

Для запуску бота потрібен API токен від Telegram. Ви можете отримати його, створивши бота через BotFather.

Створіть файл .env за прикладом .env.sample. Помістіть туди значення свого токена.

Запустіть бот

```bash
python bot.by
```