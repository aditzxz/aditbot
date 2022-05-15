#(©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>○ HAI : <a href='tg://user?id={OWNER_ID}'>pembuat botnya</a>\n○ Code : <a href='https://t.me/GROUPVIP50K'>Click here</a>\n○ Channel : @pascolgenk\n○ informasi : @testivip</b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🔒 tutup", callback_data = "tutup")
                    ]
                ]
            )
        )
    elif data == "tutup":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass