from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='💻 Kompyuter'),KeyboardButton(text='📱 Telefon')],
        [KeyboardButton(text='📺 Televizor'),KeyboardButton(text='🚖 Mashina')]
    ],
    resize_keyboard= True
)