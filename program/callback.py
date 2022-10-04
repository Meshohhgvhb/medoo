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

from driver.core import me_bot, me_user
from driver.queues import QUEUE
from driver.decorators import check_blacklist
from program.utils.inline import menu_markup, stream_markup

from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from config import (
    BOT_USERNAME,
    GROUP_SUPPORT,
    OWNER_USERNAME,
    UPDATES_CHANNEL,
    SUDO_USERS,
    OWNER_ID,
)


@Client.on_callback_query(filters.regex("home_start"))
@check_blacklist()
async def start_set(_, query: CallbackQuery):
    await query.answer("home start")
    await query.edit_message_text(
        f""" [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) ⚡~\n
╭─────────╮
│ᯓ 𝐒𝐎𝐔𝐑𝐂𝐄 ꕸ
│╭────────╯
││╔╦╦╦═╦╗╔═╦═╦══╦═╗ 
││║║║║╩╣╚╣═╣║║║║║╩╣
│╰╚══╩═╩═╩═╩═╩╩╩╩═╝
│╭ᯓтαℓαsнαηεᯓمرحبا انآ بــــوت 
││
│╰ᯓ لتشغيل الاغاني 
│ 
│╭ᯓ ❬اضف البوت الى المجموعة❭ 
││
│╰ᯓ ❬ارفع البوت ادمن في المجموعة❭
│
│╭ᯓ لتحكم ف البوت اتبع زر الاوامر
│╰────────╮
│ᯓ [𝐓𝑳𝐀𝐒𝐇𝐀𝐍𝐘](http://t.me/tlashany2)
╰─────────╯
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("ᯓاضفني للمجموعهᯓ", url=f"https://t.me/{me_bot.username}?startgroup=true"),
                ],[
                InlineKeyboardButton("𖠹s͠o͠u͠r͠c͠e͠ m͠u͠s͠i͠c͠ t͠l͠a͠s͠h͠a͠n͠y͠𖠹", url=f"https://t.me/tlashany2"),
                ],[
                    InlineKeyboardButton("ᯓطريقه التشغيلᯓ", callback_data="user_guide"),
                ],[
                    InlineKeyboardButton("الاوامر", callback_data="command_list"),
                    InlineKeyboardButton("Developer", url=f"https://t.me/{OWNER_USERNAME}")
                ],
            ]
        ),
        disable_web_page_preview=True,
    )


@Client.on_callback_query(filters.regex("user_guide"))
@check_blacklist()
async def guide_set(_, query: CallbackQuery):
    await query.answer("user guide")
    await query.edit_message_text(
        f"""
╭─────────╮
│ᯓ طريقة التشغيل، تابع في الاسفل
│╭────────╯
││╔╦╦╦═╦╗╔═╦═╦══╦═╗ 
││║║║║╩╣╚╣═╣║║║║║╩╣
│╰╚══╩═╩═╩═╩═╩╩╩╩═╝
│╭ᯓ أولا ، أضفني الى مجموعتك
││
│╰ᯓ ارفعني مشرف بصلاحيات 
│ 
│  ᯓ بعد ذالك اكتب.تحديث 
│
│╭ᯓ انضم لدعوه الحساب المساع
│╰────────╮
│ᯓ 𝐓𝑳𝐀𝐒𝐇𝐀𝐍𝐘 ꕸ
╰─────────╯
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("-› ", callback_data="home_start")
                ],
            ]
        ),
    )


@Client.on_callback_query(filters.regex("command_list"))
@check_blacklist()
async def commands_set(_, query: CallbackQuery):
    user_id = query.from_user.id
    await query.answer("👍🏻قائمة الاوامر")
    await query.edit_message_text(
        f"""
╭─────────╮
│ᯓ 𝐒𝐎𝐔𝐑𝐂𝐄 ꕸ
│╭────────╯
││╔╦╦╦═╦╗╔═╦═╦══╦═╗ 
││║║║║╩╣╚╣═╣║║║║║╩╣
│╰╚══╩═╩═╩═╩═╩╩╩╩═
│╭ᯓ  لل اوامر ، تابع في الاسفل ↓
│╰────────╮
│ᯓ 𝐓𝑳𝐀𝐒𝐇𝐀𝐍𝐘 ꕸ
╰─────────╯

""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(" اوامر البوت", callback_data="user_command"),
                ],[             
                    InlineKeyboardButton("-› ", callback_data="home_start")
                ],
            ]
        ),
    )


@Client.on_callback_query(filters.regex("user_command"))
@check_blacklist()
async def user_set(_, query: CallbackQuery):
    await query.answer("👍🏻اوامر التشغيل")
    await query.edit_message_text(
        f"""
╭─────────╮
│ᯓ طريقة التشغيل تابع في الاسفل
│╭────────╯
││╔╦╦╦═╦╗╔═╦═╦══╦═╗ 
││║║║║╩╣╚╣═╣║║║║║╩╣
│╰╚══╩═╩═╩═╩═╩╩╩╩═╝
│╭ᯓ شغل
│╰ᯓ بالرد على ملف صوتي او اسم أغنيه
│╭ᯓ فتح كول
│╰ᯓ لصعود حساب المساعد في المكالمة
│╭ᯓ اغلاق كول
│╰ᯓ لنزول المساعد من المكالمة
│╭ᯓ تخطي 
│╰ᯓ لتخطي اغنية في التشغيل
│╭ᯓ اضبط 
│╰ᯓ  لضبط صوت حساب المساعد
│╭ᯓ فيديو 
│╰ᯓ برد على مقطع او اسم 
│╭ᯓ الانتظار 
│╰ᯓ لروية الاقائمه
│╭ᯓ ابحثلي 
│╰ᯓ لبحث فديو يوتيوب
│╭ᯓ بحث 
│╰ᯓ لتحميل اغنيه من  اليوتيوب 
│╭ᯓ كتم  
│╰ᯓ لكتم الحساب  االمساعد 
│╭ᯓ بنك 
│╰ᯓ لاظهار البنك
│╭ᯓ انضم 
│╰ᯓ لدعوه الحساب المساعد
│
│╭────────╮
│╰ᯓ𝐓𝑳𝐀𝐒𝐇𝐀𝐍𝐘 ꕸ
╰─────────╯
 """,
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("-› ", callback_data="command_list")]]
        ),
    )


@Client.on_callback_query(filters.regex("stream_menu_panel"))
@check_blacklist()
async def at_set_markup_menu(_, query: CallbackQuery):
    user_id = query.from_user.id
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("يجب ان تكون لديك صلاحيات المكالمات", show_alert=True)
    chat_id = query.message.chat.id
    user_id = query.message.from_user.id
    buttons = menu_markup(user_id)
    if chat_id in QUEUE:
        await query.answer("تم فتح لوحة التحكم 👍🏻")
        await query.edit_message_reply_markup(reply_markup=InlineKeyboardMarkup(buttons))
    else:
        await query.answer("قائمه التشغيل فارغه⚡~", show_alert=True)


@Client.on_callback_query(filters.regex("stream_home_panel"))
@check_blacklist()
async def is_set_home_menu(_, query: CallbackQuery):
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("يجب ان تكون لديك صلاحيات المكالمات", show_alert=True)
    await query.answer("control panel closed")
    user_id = query.message.from_user.id
    buttons = stream_markup(user_id)
    await query.edit_message_reply_markup(reply_markup=InlineKeyboardMarkup(buttons))


@Client.on_callback_query(filters.regex("set_close"))
@check_blacklist()
async def on_close_menu(_, query: CallbackQuery):
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("يجب ان تكون لديك صلاحيات المكالمات", show_alert=True)
    await query.message.delete()


@Client.on_callback_query(filters.regex("close_panel"))
@check_blacklist()
async def in_close_panel(_, query: CallbackQuery):
    await query.message.delete()
