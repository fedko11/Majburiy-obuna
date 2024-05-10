from typing import Any
from aiogram.filters import Filter
from config import Kanal_id
from aiogram import Bot,Dispatcher
from aiogram.types import Message



dp = Dispatcher()



class CheckSubChanel(Filter):
    async def __call__(self,message: Message,bot:Bot):
        user_status = await bot.get_chat_member(Kanal_id,message.from_user_id)
        if user_status.status in ['creator','administrator',"member"]:
            return False
        return True
    
    
    
# @dp.message(CheckSubChanel())
# async def get_chanel(message:Message):
#     kanal_link = 'https://t.me/sport_tv_uzsport_fudbol_futbol'
#     await message.answer(f"Iltimos shu kanalga obuna bo'ling <a href = '{kanal_link}'>kanal</a>",)
    