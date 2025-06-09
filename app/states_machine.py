from aiogram.fsm.state import State, StatesGroup


class DownloadStateTIVK(StatesGroup):
    url = State()
    downloading = State()


class DownloadStateYoutube(StatesGroup):
    url = State()
    format = State()
    downloading = State()