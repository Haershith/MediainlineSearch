import os
import random

from pyrogram.errors.exceptions.bad_request_400 import *
from pyrogram.errors import *
from pyrogram import Client, filters
from pyrogram.errors import *
from pyrogram.types import *

#Buttons & Msgs

DEVS_BTN = InlineKeyboardMarkup([[
                 InlineKeyboardButton('Harshith', url='https://t.me/MutyalaHarshith'),
                 InlineKeyboardButton('MHgcHat', url='https://t.me/MHgchat')
                 ],
                 [
                 InlineKeyboardButton('🔙', callback_data="back_Clbs")
                 ]]
                  )

DEVS_MG = "🌱We Are epic Developers 🌟"

helps_msg = """
⸙𝚃𝚑𝚒𝚜 𝙸𝚜 MH 𝙱𝚘𝚝𝚜 𝙷𝚎𝚕𝚙 𝚂𝚎𝚌𝚝𝚒𝚘𝚗!
How to Use me 
Ex:- `Radhe Shyam`
😂Yes It Simple Normally Send App No to bot 

"""

HelpBack_Btn = InlineKeyboardMarkup([[
                InlineKeyboardButton('🔙', callback_data="HELP_BACK")
            ]])

ENSTART_BTN = InlineKeyboardMarkup([[
                InlineKeyboardButton('🆘HELP🆘', callback_data="HELP_CLB")
            ],
            [
                InlineKeyboardButton('Harshith', url='https://t.me/MutyalaHarshith'),
                InlineKeyboardButton('👩‍💻Bot Devs👩‍💻', callback_data="DevsCallback")
            ],
            [
                InlineKeyboardButton('MHGCHAT', url='https://t.me/MHGcHaT')
            ],
            [
                InlineKeyboardButton('🔍Search here🔄', switch_inline_query_current_chat=''),
                InlineKeyboardButton('↗️Go inline↗️', switch_inline_query='')
            ],
            [ 
                InlineKeyboardButton('🔄 Switch Language', callback_data="TE_CHANGE")
            ]
        ])

ENSTART_MSG = "Hi Welcome to **Harshith Media Search Bot**🎭 ✓Click Help To more Helps⚡"

STAT_STICKER = ["CAACAgQAAxkBAAEFHRditZFgRBAPm-9bkFJUQKOjSEgxoQACfwsAAmgpeVF2roP_0GLhzykE",
                "CAACAgQAAxkBAAEFHRVitZFYQ_EPOF7Y1GenAAHZOfu6xNIAAj4MAAKd3llQRh5-qJlCwa0pBA",
                "CAACAgQAAxkBAAEFHRNitZFVEBwdq0uFJDOvDRx2IzdoCwAC5wwAAubdSFEk6BkQ4EbQ1ikE",
                "CAACAgQAAxkBAAEFHRFitZFRwzQPYrVUQkxVP4yxF2Uw3gAC4AkAAu9GYFGTgHavjO_HLikE",
                "CAACAgQAAxkBAAEFHQ9itZFNixLf7fEZICaK8DF-Li967wACUAwAAmEq4VF8xFsUvkvQXSkE"              
         ]  

CLOSE_BUTTON = InlineKeyboardMarkup([[
                InlineKeyboardButton('cloce', callback_data="cloce")
            ]])
