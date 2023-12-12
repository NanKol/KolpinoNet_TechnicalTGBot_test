"""Клавиатуры бота"""

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

import emoji


kb_menu = InlineKeyboardMarkup(inline_keyboard=
                               [[InlineKeyboardButton(text=f"Показать все аварии{emoji.emojize(':magnifying_glass_tilted_left:')}", 
                                                      callback_data="Show_Troubles")],
                                [InlineKeyboardButton(text=f"Итог по авариям{emoji.emojize(':clipboard:')}", callback_data="Count_Troubles")]
                                ])

def trouble_menu(trouble_id):
    kb_builder = InlineKeyboardBuilder()
    
    buttons = [InlineKeyboardButton(text=f"Удалить {emoji.emojize(':litter_in_bin_sign:')}", callback_data=f"Delete_Message"),
               InlineKeyboardButton(text=f"Обновить аварию{emoji.emojize(':check_box_with_check:')}", callback_data=f"Update_Trouble:{trouble_id}"),
               InlineKeyboardButton(text=f"Показать аварии{emoji.emojize(':magnifying_glass_tilted_left:')}", callback_data="Show_Troubles"),
               InlineKeyboardButton(text=f"Итог по авариям{emoji.emojize(':clipboard:')}", callback_data=f"Count_Troubles")]
    kb_builder.row(*buttons, width=2)
    
    return kb_builder.as_markup()
    
count_trables_menu = InlineKeyboardMarkup(inline_keyboard=
                                          [[InlineKeyboardButton(text="Обновить", callback_data=f"Update_Count_Trouble"),],])