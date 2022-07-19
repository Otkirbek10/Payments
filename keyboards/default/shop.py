from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='💻 Kompyuter'),KeyboardButton(text='📱 Telefon')],
    ],
    resize_keyboard= True
)