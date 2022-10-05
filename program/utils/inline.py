""" inline section button """


from pyrogram.types import (
  InlineKeyboardButton,
  InlineKeyboardMarkup,
)


def stream_markup(user_id):
  buttons = [
    [
      InlineKeyboardButton(text="⚡~تحكم", callback_data=f'stream_menu_panel | {user_id}'),
      InlineKeyboardButton(text="⚡~اغلاق", callback_data=f'set_close'),
      ],
    [ 
     InlineKeyboardButton("𖠹s͠o͠u͠r͠c͠e͠ m͠u͠s͠i͠c͠ t͠l͠a͠s͠h͠a͠n͠y͠𖠹", url=f"https://t.me/tlashany2"),
    ],
  ]
  return buttons


def menu_markup(user_id):
  buttons = [
    [
      InlineKeyboardButton(text="⏹", callback_data=f'set_stop | {user_id}'),
      InlineKeyboardButton(text="⏸", callback_data=f'set_pause | {user_id}'),
      InlineKeyboardButton(text="▶️", callback_data=f'set_resume | {user_id}'),
      InlineKeyboardButton(text="⏭", callback_data=f'set_skip | {user_id}'),
    ],
    [
      InlineKeyboardButton(text="🔇", callback_data=f'set_mute | {user_id}'),
      InlineKeyboardButton(text="🔊", callback_data=f'set_unmute | {user_id}'),
    ],
    [
      InlineKeyboardButton("𖠹s͠o͠u͠r͠c͠e͠ m͠u͠s͠i͠c͠ t͠l͠a͠s͠h͠a͠n͠y͠𖠹", url=f"https://t.me/tlashany2"),
      ],
    [ 
      InlineKeyboardButton(text="رجوع", callback_data='stream_home_panel'),
    ]
  ]
  return buttons


close_mark = InlineKeyboardMarkup(
  [
    [
      InlineKeyboardButton(
        "اغلاق", callback_data="set_close"
      )
    ]
  ]
)


back_mark = InlineKeyboardMarkup(
  [
    [
      InlineKeyboardButton(
        "⚡~رجوع", callback_data="stream_menu_panel"
      )
    ]
  ]
)
