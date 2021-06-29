# lazyleech - Telegram bot primarily to leech from torrents and upload to Telegram
# Copyright (c) 2021 lazyleech developers <theblankx protonmail com, meliodas_bot protonmail com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

# (C) @FayasNoushad

import os
from pyrogram import Client, filters
from .. import ADMIN_CHATS, ALL_CHATS
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from telegraph import upload_file

@Client.on_message(filters.command('telegraph') & filters.chat(ALL_CHATS))
async def getmedia(bot, update):
    reply = message.reply_to_message
    document = message.document
    photo = message.photo
    thumbset = False
    user_id = message.from_user.id
    medianame = "./DOWNLOADS/" + str(update.from_user.id) + "/FayasNoushad/FnTelegraphBot"
    
    if document or photo:
        message = await message.reply_text(
            text="Processing...",
            disable_web_page_preview=True
        )
        await bot.download_media(
            message=update,
            file_name=medianame
        )
        response = upload_file(medianame)
        try:
            os.remove(medianame)
        except:
            pass
    except Exception as error:
        print(error)
        text=f"Error :- <code>{error}</code>"
        await message.reply_text(
            text=text,
            disable_web_page_preview=True,
            reply_markup=reply_markup
        )
        return
    text=f"Link: https://telegra.ph{response[0]}"
    reply_markup=InlineKeyboardMarkup(
        [[
        InlineKeyboardButton(text="Open Link", url=f"https://telegra.ph{response[0]}"),
        InlineKeyboardButton(text="Share Link", url=f"https://telegram.me/share/url?url=https://telegra.ph{response[0]}")
        ]]
    )
    await message.reply_text(
        text=text,
        disable_web_page_preview=True,
        reply_markup=reply_markup
    )
