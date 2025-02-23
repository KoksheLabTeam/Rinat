from aiogram import Bot, Dispatcher
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, WebAppInfo
from aiogram.filters import Command
from aiogram import Router

bot = Bot('')
dp = Dispatcher()

router = Router()
dp.include_router(router)

@router.message(Command("start"))
async def start(message):

    button = KeyboardButton(
        text='Открыть веб страницу',
        web_app=WebAppInfo(url='https://example.com')
    )
    markup = ReplyKeyboardMarkup(
        keyboard=[[button]],
        resize_keyboard=True
    )

    await message.answer('Привет! Рады видеть вас!', reply_markup=markup)

if __name__ == '__main__':
    import asyncio
    asyncio.run(dp.start_polling(bot))











