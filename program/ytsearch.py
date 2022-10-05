"""
Video + Music Stream Telegram Bot
Copyright (c) 2022-present levina=lab <https://github.com/levina-lab>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but without any warranty; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <https://www.gnu.org/licenses/licenses.html>
"""


from config import BOT_USERNAME
from driver.decorators import check_blacklist
from driver.filters import command
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from youtube_search import YoutubeSearch


@Client.on_message(command(["رابط", f"search@{BOT_USERNAME}"]) & ~filters.edited)
@check_blacklist()
async def youtube_search(_, message: Message):
    if len(message.command) < 2:
        return await message.reply_text("/search **needs an argument !**")
    query = message.text.split(None, 1)[1]
    m = await message.reply_text("**⚡**")
    results = YoutubeSearch(query, max_results=5).to_dict()
    text = ""
    for i in range(5):
        try:
            text += f"-› **الاسم:** __{results[i]['title']}__\n"
            text += f"-› **المدو:** `{results[i]['duration']}`\n"
            text += f"-› **المشاهدات:** `{results[i]['views']}`\n"
            text += f"-› **القناة:** {results[i]['channel']}\n"
            text += f"-› **الرابط:** https://www.youtube.com{results[i]['url_suffix']}\n\n"
        except IndexError:
            break
    await m.edit_text(
        text,
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("مسح", callback_data="close_panel")]]
        ),
    )
@Client.on_message(commandpro(["السورس", "سورس"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/1838d6ee695608a4fff29.jpg",
        caption=f"""
        
╭─────────╮
│ᯓ [𝐒𝐎𝐔𝐑𝐂𝐄](http://t.me/tlashany2)
│╭────────╯
││[╔╦╦╦═╦╗╔═╦═╦══╦═╗]](http://t.me/m_e_s_h_o)
││[║║║║╩╣╚╣═╣║║║║║╩╣](http://t.me/tlashany2)
│╰[╚══╩═╩═╩═╩═╩╩╩╩═╝](http://t.me/tlashany3)
│╭ᯓ you are now 
│╰ᯓ in the source 
│╭ᯓ tlashany music 
│╰ᯓ to play music 
│╭ᯓ Telegram bot 
│╰────────╮
│ᯓ [𝐓𝑳𝐀𝐒𝐇𝐀𝐍𝐘](http://t.me/tlashany2)
╰─────────╯
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("𖠹s͠o͠u͠r͠c͠e͠ m͠u͠s͠i͠c͠ t͠l͠a͠s͠h͠a͠n͠y͠𖠹", url=f"https://t.me/tlashany2"),
                ],[
                    InlineKeyboardButton("𖠹يـوزرات تـلاشـانــي𖠹", url=f"https://t.me/tlashany3"),
                ],[ 
                InlineKeyboardButton("P꯭R꯭O꯭G꯭R꯭A꯭M꯭M꯭E꯭R꯭ T꯭L꯭A꯭S꯭H꯭A꯭N꯭Y꯭ 𖠜", url=f"https://t.me/m_e_s_h_o")
                ]
            ]
        ),
    )
