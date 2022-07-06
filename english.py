import os
import random

from pyrogram.errors.exceptions.bad_request_400 import *
from pyrogram.errors import *
from pyrogram import Client, filters
from pyrogram.errors import *
from pyrogram.types import *

#Buttons & Msgs

DEVS_BTN = InlineKeyboardMarkup([[
                 InlineKeyboardButton('💞 Harshith', url='https://t.me/MutyalaHarshith'),
                 InlineKeyboardButton('🥳 MHgcHat', url='https://t.me/MHgchat')
                 ],
                 [
                 InlineKeyboardButton('👋 Back', callback_data="back_Clbs")
                 ]]
                  )

DEVS_MG = "✨ Hai Iam Mutyala Harshith 💞"

helps_msg = """
⸙𝚃𝚑𝚒𝚜 𝙸𝚜 MH 𝙱𝚘𝚝𝚜 𝙷𝚎𝚕𝚙 𝚂𝚎𝚌𝚝𝚒𝚘𝚗!
How to Use me 
Ex:- `Radhe Shyam`
😂Yes It Simple Normally Movie Search bot 

"""

HelpBack_Btn = InlineKeyboardMarkup([[
                InlineKeyboardButton('👋 BacK', callback_data="HELP_BACK")
            ]])

ENSTART_BTN = InlineKeyboardMarkup([[
                InlineKeyboardButton('😜 Help', callback_data="HELP_CLB")
            ],
            [
                InlineKeyboardButton('💞 Harshith', url='https://t.me/MutyalaHarshith'),
                InlineKeyboardButton('🤩 Develovepers', callback_data="DevsCallback")
            ],
            [
                InlineKeyboardButton('💞 MHGcHaT', url='https://t.me/MHGcHaT')
            ],
            [
                InlineKeyboardButton('🔍Search here🔄
', switch_inline_query_current_chat=''),
                InlineKeyboardButton('💡 Go inline', switch_inline_query='')
            ],
            [ 
                InlineKeyboardButton('😘 Change Language', callback_data="TE_CHANGE")
            ]
        ])

ENSTART_MSG = "Hi Welcome to **Harshith Media Search Bot**🎭 ✓Click Help To more Helps⚡"

STAT_STICKER = ["CAACAgUAAxkBAAIaoGLFAh4HC8weC0J4x1c3HAVnoxSsAAJLBQACk63ZVTl1b7fDo-OpHgQ",
                "CAACAgUAAxkBAAIapGLFAlREvYMW3VfKH7VwhIBeaafMAAIvBQACaXfYVQXRbSbmknymHgQ",
                "CAACAgUAAxkBAAIanWLFAhD1jogzet85akKM_JwwhWnkAAJyBwACJrrZVf2J1QcUBqdVHgQ",
                "CAACAgUAAxkBAAIammLFAfvd9RBuotbZunrvn1lIU8kLAAIhBgAC3ZD5V8DbuSeu9KvqHgQ",
                "CAACAgUAAxkBAAIal2LFAeiA5Hb6vW9dBlgQmx_UVpT0AAI9AwAClKrpVqYLvURyUjbVHgQ"              
         ]  

CLOSE_BUTTON = InlineKeyboardMarkup([[
                InlineKeyboardButton('cloce', callback_data="cloce")
            ]])
