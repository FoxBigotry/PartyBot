from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from databasa.db_connection import connect_insert

router = Router()

class user_data(StatesGroup):
    height = State()
    weight = State()

@router.message(CommandStart())
async def step_one_height(message: Message, state: FSMContext):
    await state.set_state(user_data.height)
    await message.answer('Привет!\nМне нужно записать Ваши данные.\nВведите Ваш рост, в см')

@router.message(user_data.height)
async def step_two_weight(message: Message, state: FSMContext):
    await state.update_data(height=message.text)
    await state.set_state(user_data.weight)
    await message.answer('Введите Ваш вес, в кг')

@router.message(user_data.weight)
async def step_three_save(message: Message, state: FSMContext):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    await connect_insert(message.from_user.id,data["height"],data["weight"])
    await message.answer(f'Спасибо за Ваши данные.\nВаш id: {message.from_user.id}\nВаш рост: {data["height"]} см\nВаш вес: {data["weight"]} кг')
    await state.clear()
