import os
import random

from pyrogram.errors.exceptions.bad_request_400 import *
from pyrogram.errors import *
from pyrogram import Client, filters
from pyrogram.errors import *
from pyrogram.types import *

STARTCMD = "🌼Choose language To Start bot!"

COMMAND_LANGBTN = InlineKeyboardMarkup([[
      InlineKeyboardButton('English', callback_data="START_EN")
      ],
      [
      InlineKeyboardButton('తెలుగు', callback_data="START_TE")
      ]])

#=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•Mutyala Harshith 2022© All Rights Resived•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=#
#START_TE Callback Text & Btn

TE_HELP = InlineKeyboardMarkup([[
                InlineKeyboardButton('ముందు జాబితాకు ప్రవేశించండి', callback_data="HELP_BACK")
            ]])

TE_STARB = InlineKeyboardMarkup([[
                InlineKeyboardButton('సహాయం❔', callback_data="TEHELP_CLB")
            ],
            [
                InlineKeyboardButton('🔥మన డేటాబేస్ ఒకటి🔥', url='https://t.me/Telugu_Robots'),
                InlineKeyboardButton('🤪బోట్ డివలోపర్స్🤩', callback_data="TE_Devs")
            ],
            [
                InlineKeyboardButton('✨Mutyala Harshith💞', url='https://t.me/MutyalaHarshith')
            ],
            [
                InlineKeyboardButton('🔍ఇక్కడ సెర్చ్', switch_inline_query_current_chat=''),
                InlineKeyboardButton('💞 సెర్చ్ ఇన్లైన్', switch_inline_query='')
            ],
            [
                InlineKeyboardButton('🔄Switch Language', callback_data="CHANGE_LNG")
            ]
        ])

TE_STARTM = "Hi సాదరంగా స్వీకరించండి **Harshith Media search Bot**🎭 ✓వెడిదూర సహాయం కోసం సహాయం క్లిక్ చేయండి⚡"

#=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•Harshith 2022© All Rights Resived•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=#
TEHELP_MSG = """
⸙ మీకు అవసరమైన సినిమా అందుబాటులో ఉంది!

**📖ఇలా ఆప్ సెర్చ్ చేయండి ?**
మీకు అవసరమైన యాప్ పేరు అందజేయండి

ఉదాహరణ- `రాధే శ్యామ్`

🪶సాధారణ బోట్‌కి ఇలా ప్రత్యుత్తరం ఇవ్వండి మరియు మీకు లభించే మెను ద్వారా మీరు మీ ఆర్డర్‌ను పొందవచ్చు!


➡బాట్ రన్ అవుతుంది మా డేటాబేస్ ఒకటి
➡మాకు జాబితాలో ఉంది,
      ▪సినిమాలు
      ▪బోట్స్
      ▪ఇతర ఫీచర్స్

➡ఈ బాట్ ఇన్‌లైన్ పద్ధతిని ఉపయోగించడం అత్యంత విజయవంతమైనది.

✔ Stylish Text 
     ▫ @StylishTextRoBoT
✔Filter BoT Extra 
     ▫ @MHBEASTBOT
✔Filter BoT 
     ▫ @MutyalaHarshithBoT
     
       `@MutyalaHarshith and @MHGcHaT`
"""

TEHelp_backbtn = InlineKeyboardMarkup([[
                InlineKeyboardButton('వెనుకకి', callback_data="TEHELP_BACK")
            ]])


DEVS_BTNTE = InlineKeyboardMarkup([[
                 InlineKeyboardButton('Updates', url='https://t.me/MutyalaHarshith'),
                 InlineKeyboardButton('Support', url='https://t.me/MHGcHaT')
                 ],
                 [
                 InlineKeyboardButton('తిరిగి 🔙', callback_data="TEDEVS_BAC")
                 ]]
                  )

DEVS_MGTE = """ 
మేము తయారుచేసే😎 బోట్ కి ఎటువంటి కాపీరైట్స్ వేయకండి?
మీకు ఇష్టం లేకపోతే ఈ బోట్ వాడకండి 😑
మీకు ఎటువంటి సమస్య లేకుండా చూసుకుంటాం 👍
నన్ను తయారు చేసినందుకు ముత్యాల హర్షిత్ థాంక్స్
"""


