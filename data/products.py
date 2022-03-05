from aiogram import types
from aiogram.types import LabeledPrice
from utils.misc.produc import Product


macbook = Product(
    title="Ноутбук Apple MacBook Air 2020 (2560x1600, Apple M1 3.2 ГГц, RAM 8 ГБ, SSD 256 ГБ, Apple graphics 7-core)",
    description="To'lov qilish uchun quyidagi tugmani bosing.",
    currency="UZS",
    prices=[
        LabeledPrice(
            label='MacBook Air',
            amount=1280050000, 
        ),
        LabeledPrice(
            label='Yetkazib berish (7 kun)',
            amount=2000000,
        ),
    ],
    start_parameter="create_invoice_macbook",
    photo_url='https://bit.ly/3pYG7eV',
    photo_width=1280,
    photo_height=724,
    need_email=True,
    need_name=True,
    need_phone_number=True,
    need_shipping_address=True, 
    is_flexible=True,
)

REGULAR_SHIPPING = types.ShippingOption(
    id='post_reg',
    title="Fargo (3 kun)",
    prices=[
        LabeledPrice(
            'Maxsus quti', 1000000),
        LabeledPrice(
            '3 kunda yetkazish', 2500000),
    ]
)
FAST_SHIPPING = types.ShippingOption(
    id='post_fast',
    title='Express pochta (1 kun)',
    prices=[
        LabeledPrice(
            '1 kunda yetkazish', 3000000),
    ]
)

PICKUP_SHIPPING = types.ShippingOption(id='pickup',
                                       title="Do'kondan olib ketish",
                                       prices=[
                                           LabeledPrice("Yetkazib berishsiz", -3000000)
                                       ])























































# from aiogram import types
# from aiogram.types import LabeledPrice
# from utils.misc.product import Product
# macbook = Product(
#     title="Ноутбук Apple MacBook Air 2020 (2560x1600, Apple M1 3.2 ГГц, RAM 8 ГБ, SSD 256 ГБ, Apple graphics 7-core)",
#     description="To'lov qilish uchun quyidagi tugmani bosing",
#     currency="UZS",
#     prices=[
#         LabeledPrice(
#             label='MacBook Air',
#             amount=1221050000,
#         ),
#         LabeledPrice(
#             label='Yetkazib berish (7 kun)',
#             amount=1500000,
#         ),
#     ],
#     start_parameter="create_invoice_macbook"
#     photo_url="https://ru.depositphotos.com/stock-photos/macbook-air.html?qview=48861567",
#     photo_width=5100
#     photo_height=3100
#     need_email=True,
#     need_name=True,
#     need_phone_number=True,
#     need_shipping_address=True,
#     is_flexible=True,
# )
# REGULAR_SHIPPING = types.ShippingOption(
#     id = 'post_reg',
#     title="Fargo(3-kun)",
#     prices=[
#         LabeledPrice(
#             'Maxsus quti',1000000),
#         LabeledPrice(
#             '3 kunda yetkazish',2500000,
#         )
#     ]
# )

# FAST_SHIPPING = types.ShippingOption(
#     id = 'fast',
#     title='Express pochta (1 kun)',
#     prices=[
#         LabeledPrice(
#             "1 kunda yetkazish",3000000),
#     ]
# )


# PICKUP_SHIPPING = types.ShippingOption(id='pickup',
#                                        title="Do'kondan olib ketish",
#                                        prices=[
#                                            LabeledPrice("Yetkazib berishsiz", -5000000)
#                                        ])