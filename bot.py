import asyncio
from app.handlers import router
from aiogram import Bot, Dispatcher
import shutil
TOKEN = ""


async def main():
    bot = Bot(token=TOKEN)
    dp = Dispatcher()
    try:
        shutil.rmtree("current_videos")
    except:
        pass
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Бот остановлен!")
