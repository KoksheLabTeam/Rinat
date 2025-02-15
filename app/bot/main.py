from aiogram import Bot, Dispatcher
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, WebAppInfo
from aiogram.filters import Command
from aiogram import Router

bot = Bot('7105803545:AAEuXRFep1TdMyM5_UI5HjcOxA_K4D3bNig')
dp = Dispatcher()

router = Router()
dp.include_router(router)

@router.message(Command("start"))
async def start(message):

    button = KeyboardButton(
        text='Открыть веб страницу',
        web_app=WebAppInfo(url='https://github.com/KoksheLabTeam/Rinat/blob/main/app/bot/main.py')
    )
    markup = ReplyKeyboardMarkup(
        keyboard=[[button]],
        resize_keyboard=True
    )

    await message.answer('Привет! Рады видеть вас!', reply_markup=markup)

if __name__ == '__main__':
    import asyncio
    asyncio.run(dp.start_polling(bot))











