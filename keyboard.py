from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


main_kb = [
    [KeyboardButton(text='Худи'),
     KeyboardButton(text='Кроссовки')],
    [KeyboardButton(text='Пуховики'),
     KeyboardButton(text='Куртки')]
]

brandkrs_kb = [
    [KeyboardButton(text='Nike'),
     KeyboardButton(text='Stone Island')],
    [KeyboardButton(text='Burberry'),
     KeyboardButton(text='Saint Laurent')]
]

nike_kb = [
    [KeyboardButton(text='Air ZOOMX VAPORFLY'),
     KeyboardButton(text='Air Max 90 GTX')],
    [KeyboardButton(text='AIR MAX TERRASCAPE 90 NN'),
     KeyboardButton(text='Air Jordan')]
]


admin_kb = [
    [KeyboardButton(text='123')],
    [KeyboardButton(text='321')]
]


brandkrs = ReplyKeyboardMarkup(keyboard=brandkrs_kb,
                           resize_keyboard=True,
                           input_field_placeholder='Выберете бренд который вам интересен')

nike = ReplyKeyboardMarkup(keyboard=nike_kb,
                           resize_keyboard=True,
                           input_field_placeholder='Выберете обувь который вам интересна')


admin = ReplyKeyboardMarkup(keyboard=admin_kb,
                           resize_keyboard=True,
                           input_field_placeholder='aiogram3')

main = ReplyKeyboardMarkup(keyboard=main_kb,
                           resize_keyboard=True,
                           input_field_placeholder='Выберете товар который вам интересен')

cont = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='VK', url='https://vk.com/kkuriiov')],
    [InlineKeyboardButton(text='Telegram', url='https://t.me/qwerty375')]
])

repo = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Translit', url='https://github.com/Ki5BoY/translit')],
    [InlineKeyboardButton(text='TG_Bot', url='https://github.com/Ki5BoY/fictional-garbanzo')]
])
