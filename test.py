import os
import time

from ntgcalls import InputMode
from telethon import TelegramClient

from pytgcalls import idle
from pytgcalls import PyTgCalls
from pytgcalls.types.input_stream import AudioStream
from pytgcalls.types.input_stream import Stream

app = TelegramClient(
    'pytgcalls',
    api_id=28509031,
    api_hash='86a341f619e093b8b2168dad9844c0db',
)

call_py = PyTgCalls(app)
call_py.start()
file = './input.raw'
while not os.path.exists(file):
    time.sleep(0.125)
call_py.join_group_call(
    4087109494,
    Stream(
        AudioStream(
            input_mode=InputMode.File,
            path=file,
        ),
    ),
)
idle()