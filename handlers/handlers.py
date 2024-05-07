from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message, ContentType
from database.db_connection import connect_insert

from aiogram.types import KeyboardButton, WebAppInfo, ReplyKeyboardMarkup

router = Router()


@router.message(CommandStart())
async def step_one_height(message: Message):
    item1 = KeyboardButton(text='Анкета',web_app=WebAppInfo(url='https://7c1c-95-172-139-97.ngrok-free.app/webapp'))
    keyboard = ReplyKeyboardMarkup(keyboard=[[item1]], resize_keyboard=True)
    await message.answer('Привет!\nМне нужно записать Ваши данные.\nВоспользуйтесь кнопкой "Анкета"', reply_markup=keyboard)


@router.message()
async def handle_web_app_data(message: ContentType.WEB_APP_DATA):
    web_app_data = message.web_app_data.data
    data = web_app_data.split('&')
    height_value = None
    weight_value = None
    for item in data:
        key, value = item.split('=')
        if key == 'height':
            height_value = value
        elif key == 'weight':
            weight_value = value
    await connect_insert(message.from_user.id, height_value, weight_value)
    await message.answer(f'Спасибо за Ваши данные.\nВаш id: {message.from_user.id}\nВаш рост: {height_value} см\nВаш вес: {weight_value} кг')