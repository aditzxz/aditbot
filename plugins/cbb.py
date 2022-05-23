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
            text = f"<b>○ ᴀᴋᴜ ᴀᴅᴀʟᴀʜ : <a href='tg://user?id={OWNER_ID}'>ᴄʀᴇᴀᴛᴏʀ ʙᴏᴛ</a>\n○ •ɪɴғᴏ• : <a href='https://t.me/GROUPVIP50K'>Click here</a>\n○ •ᴄʜᴀɴɴᴇʟ• : @pascolgenk\n○ •ɪɴғᴏʀᴍᴀsɪ• : https://t.me/viptesti/187</b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("💥 Close 💥", callback_data = "Tutup")
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
