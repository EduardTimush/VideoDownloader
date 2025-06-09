from aiogram.types import (KeyboardButton, ReplyKeyboardMarkup,
                           InlineKeyboardMarkup, InlineKeyboardButton)

keyboard = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="TikTok")],
                                         [KeyboardButton(text="Instagram"), KeyboardButton(text="VK")]],
                               resize_keyboard=True,
                               input_field_placeholder="Выбери соц-сеть")

inline_keyboard = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Видео", callback_data="video"),
                                                         InlineKeyboardButton(text="Без звука", callback_data="no_audio"),
                                                         InlineKeyboardButton(text="Аудио", callback_data="audio")]])