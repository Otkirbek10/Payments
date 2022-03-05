from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton

def sozdat_knopka(product):
    keys=InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="Xarid qilish",callback_data=f"Product:{product}"),

        ]
    ])
    return keys