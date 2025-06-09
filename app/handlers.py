from aiogram import Router, F
from aiogram.enums import ParseMode
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery, FSInputFile
from aiogram.filters import CommandStart, Command
from aiogram.utils.formatting import Text

from app.states_machine import DownloadStateTIVK, DownloadStateYoutube
from downloaders.video import VideoDownloader
from downloaders.youtube import YoutubeDownloader
import os
import app.reply_keyboard as reply_keyboard

down_state_tivk = DownloadStateTIVK
down_state_youtube = DownloadStateYoutube

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer("Привет🤝\nЭто инновационный бот по скачиванию видео с TikTok, Instagram, VKontakte... 🆕\nВозможность скачивания с YouTube в разработке.↘\nЕсли найдете какие-то ошибки в работе бота, прошу оповестить меня! 🧏\n@sovetskijcactus🥸", reply_markup=reply_keyboard.keyboard)


@router.message(F.text == "TikTok")
async def tiktok(message: Message, state: FSMContext):
    await state.set_state(down_state_tivk.url)
    await message.answer(text="🖇Отправляй ссылку на видео:")
    global downloader
    downloader = VideoDownloader


@router.message(F.text == "Instagram")
async def inst(message: Message, state: FSMContext):
    await state.set_state(down_state_tivk.url)
    await message.answer(text="🖇Отправляй ссылку на видео:")
    global downloader
    downloader = VideoDownloader


@router.message(F.text == "VK")
async def vk(message: Message, state: FSMContext):
    await state.set_state(down_state_tivk.url)
    await message.answer(text="🖇Отправляй ссылку на видео:")
    global downloader
    downloader = VideoDownloader


@router.message(down_state_tivk.url)
async def url_downloader(message: Message, state: FSMContext):
    execute_down = downloader(message.text, message.chat.id)
    waiting = FSInputFile(path="app/gif/loading-thinking.gif", filename="waiting.gif")
    await message.answer_animation(animation=waiting)
    if execute_down == True:
        await message.answer(text="📨Готово. Отправляю видео....")
        video = FSInputFile(path=rf"current_videos/{message.chat.id}.mp4", filename="hz.mp4")
        await message.answer_video(video=video)
        os.remove(f"current_videos/{message.chat.id}.mp4")
    else:
        await message.answer("🤬Ошибка скачивания, повтори попытку или проверь ссылку и выбранную соц. сеть. Если не помогло, пиши \n@sovetskijcactus")
    await state.clear()


@router.message(F.text == "!YouTube!")
async def youtube(message: Message, state: FSMContext):
    await state.set_state(down_state_youtube.url)
    await message.answer(text="🗂Выбери нужный тебе формат:", reply_markup=reply_keyboard.inline_keyboard)
    global downloader
    downloader = YoutubeDownloader


@router.callback_query(F.data == "video")
async def youtube_get_data(callback: CallbackQuery, state: FSMContext):
    await state.set_state(down_state_youtube.format)
    await callback.answer("Принято!")
    await callback.message.answer(text="🖇Отправляй ссылку на видео:")
    global down_format
    down_format = 0


@router.callback_query(F.data == "no_audio")
async def youtube_get_data(callback: CallbackQuery, state: FSMContext):
    await state.set_state(down_state_youtube.format)
    await callback.answer("Принято!")
    await callback.message.answer(text="🖇Отправляй ссылку на видео:")
    global down_format
    down_format = 1

@router.callback_query(F.data == "audio")
async def youtube_get_data(callback: CallbackQuery, state: FSMContext):
    await state.set_state(down_state_youtube.format)
    await callback.answer("Принято!")
    await callback.message.answer(text="🖇Отправляй ссылку на видео:")

    global down_format
    down_format = 2


@router.message(down_state_youtube.format)
async def url_downloader(message: Message, state: FSMContext):
    waiting = FSInputFile(path = "app/gif/loading-thinking.gif", filename="waiting.gif")
    await message.answer_animation(animation=waiting)
    execute_down = downloader(url=message.text, title=message.chat.id, down_format=down_format)
    if execute_down ==True:
        await message.answer(text="📨Готово. Отправляю видео....")
        await message.answer(text="😮Погоди малеха...:)")
        if down_format == 0:
            video = FSInputFile(path=rf"current_videos/{message.chat.id}.mp4",
                                filename="hz.mp4")
            await message.answer_video(video=video)
            os.remove(f"current_videos/{message.chat.id}.mp4")
        if down_format == 1:
            video = FSInputFile(path=rf"current_videos/{message.chat.id}.mp4",
                                filename="audio.mp4")
            await message.answer_video(video=video)
            os.remove(f"current_videos/{message.chat.id}.mp4")
        elif down_format == 2:
            audio = FSInputFile(path=rf"current_videos/{message.chat.id}.mp3",
                                filename="audio.mp3")
            await message.answer_audio(audio=audio)
            os.remove(f"current_videos/{message.chat.id}.mp3")
    else:
        await message.answer("🤬Ошибка скачивания, повтори попытку или проверь ссылку и выбранную соц. сеть. Если не помогло, пиши \n@sovetskijcactus")

    await state.clear()


@router.message(Command("info"))
async def cmd_info(message: Message):
    await message.answer("Начинающий разработчик с большими амбициями!🤗\n"
                        "Всегда буду рад Вашей поддержке по комманде /donate💵\n"
                        "Надеюсь боь принес пользу🚀\n"
                        "Любые предложения и комментарии @sovetskijcactus🌵\n"
                        "Удачи, кэп!🫡\n"
                        )


@router.message(Command("donate"))
async def cmd_donate(message: Message):
    text = "USDT TRC20 `TF72EjdBWtDf3wmizjk9NrE5dbebqQgneR`\nUSDT TON `EQBu3O3khamnM90MkjWFP-a_Er7Iy2lJpkj6Ild_ZZ63Yvox`\nАПБ Переводилка \\- `37377959262`\nОтдельная благодарность всем, кто оценил мой труд в денежном эквиваленте, спасибо комрады🤝"
    await message.answer(text, parse_mode=ParseMode.MARKDOWN_V2)

@router.message(Command("share"))
async def cmd_share(message: Message):
    text = ("""<b>https://t.me/GrabThatVidBot</b>\n<b>Друг</b>, с тобой поделились ссылкой\nна инновационного бота по загрузке видео без водяных знаков \nC <b>САМЫХ ПОПУЛЯРНЫХ СОЦ. СЕТЕЙ</b>.\nЕсли бот оказался полезным, для поддержки работы сервиса\nпоодержи меня по команде /donate в боте."""
    )
    await message.answer(text, parse_mode=ParseMode.HTML)
