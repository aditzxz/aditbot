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
            text = f"<b>○ ᴘᴇᴍɪʟɪᴋ : <a href='tg://user?id={OWNER_ID}'>ʙᴏᴛ ɪɴɪ</a>\n○ •ɢʀᴏᴜᴘ• : <a href='https://t.me/penikmatvidioo'>Click here</a>\n○ •ᴄʜᴀɴɴᴇʟ• : <a href='https://t.me/pascolgenk'>Click here</a>\n○ •ᴋᴏɴᴛᴇɴ ᴘʀᴇᴍɪᴜᴍ• : <a href='https://t.me/viptesti/187'>Click here</a></b>",
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
