from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

til = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🇷🇺 Русский", callback_data="rus")
        ],
        [
            InlineKeyboardButton(text="🇺🇿 O'zbekcha", callback_data="uzb")
        ]
    ]
)