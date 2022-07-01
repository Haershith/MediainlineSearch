import re
import uuid
import socket
import platform
import time
import math
import json
import string
import traceback
import psutil
import asyncio
import wget
import motor.motor_asyncio
import pymongo
import aiofiles
import datetime
import os
import random
import logging
from telugu import *
from english import *
from pyrogram.errors.exceptions.bad_request_400 import *
from pyrogram.errors import *
from pyrogram.types import *
from helper.decorators import humanbytes
from asyncio import *
import requests
from utils.database import Database
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.types import *
from pyrogram.types import Message

from info import START_MSG, CHANNELS, ADMINS, INVITE_MSG, DATABASE_URI, PRIVATE_LOG
from utils import Media, unpack_new_file_id


#=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=Harshith 2022© All Rights Resived•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=#
#Callbacks

@Client.on_callback_query()  
async def tgm(bot, update):  
    if update.data == "add": 
        await update.answer(
             text="Harshith Devs",
        )
    elif update.data == "START_EN":
         await update.message.edit_text(
             text=ENSTART_MSG,
             reply_markup=ENSTART_BTN,
             disable_web_page_preview=True
         )
         await update.answer(
             text="Bot Started In English",
         )  
    elif update.data == "HELP_CLB":
         await update.message.edit_text(
             text=helps_msg,
             reply_markup=HelpBack_Btn
         )
         await update.answer(
             text=" Welcome to Help Menu 🌱"
         )
    elif update.data == "HELP_BACK":
         await update.message.edit_text(
             text=ENSTART_MSG,
             reply_markup=ENSTART_BTN
         )
         await update.answer(
             text="Help Menu Backed 🖐️"
         )
    elif update.data == "DevsCallback":
         await update.message.edit_text(
             text=DEVS_MG,
             reply_markup=DEVS_BTN
         )
         await update.answer(
             text="Mutyala Harshith"
         )
    elif update.data == "TE_CHANGE":
         await update.message.edit_text(
             text=STARTCMD,
             reply_markup=COMMAND_LANGBTN
         )
         await update.answer(
             text="Switch Language 🔄"
         )
    elif update.data == "START_TE":
         await update.message.edit_text(
             text=TE_STARTM,
             reply_markup=TE_STARB
         )
         await update.answer(
             text="స:మేముట మేము స:ట😏"
         )
    elif update.data == "TEHELP_CLB":
         await update.message.edit_text(
             text=TEHELP_MSG,
             reply_markup=TEHelp_backbtn
         )
         await update.answer(
             text="అయి బొక్కగానే ఈ సహాయం"
         )
    elif update.data == "TEHELP_BACK":
         await update.message.edit_text(
             text=TE_STARTM,
             reply_markup=TE_STARB
         )
         await update.answer(
             text="ఈ సుఖ ప్రపంచే 🤭"
         )
    elif update.data == "TE_Devs":
         await update.message.edit_text(
             text=DEVS_MGTE,
             reply_markup=DEVS_BTNTE
         )
         await update.answer(
             text="గామ్మెక్ అంటే గ్రీన్😌"
         )
    elif update.data == "TEDEVS_BAC":
         await update.message.edit_text(
             text=TE_STARTM,
             reply_markup=TE_STARB
         )
         await update.answer(
             text="ఈ సుఖ ప్రపంచే 🤭"
         )
    elif update.data == "CHANGE_LNG":
         await update.message.edit_text(
             text=STARTCMD,
             reply_markup=COMMAND_LANGBTN
         )
         await update.answer(
             text="ఈ సుఖ ప్రపంచే 🤭"
         )
    elif update.data == "back_Clbs":
         await update.message.edit_text(
             text=ENSTART_MSG,
             reply_markup=ENSTART_BTN
         )
         await update.answer(
             text="Menu Backed 🔙"
         )
    elif update.data == "cloce":
        await update.message.delete()

#=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=

print("Callback.py Started Successfully 🌱🔥")
