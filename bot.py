from pyrogram import Client, filters
import aiohttp
from config import 27143201, 553091f2b29f1c827fb4fca91c49b313, 6791456280:AAFNmdzA8XwO_FCehG3y_PghIVQKc2gCvgM, b6c46ec4e64ba5067ed4386d2436dc1dad332db9, https://vikfy.com/member/tools/api, Vikfy_Support, vikfy_official, vikfy
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

bot = Client('AdlinkFly shortener bot',
             api_id=27143201,
             api_hash=553091f2b29f1c827fb4fca91c49b313,
             bot_token=6791456280:AAFNmdzA8XwO_FCehG3y_PghIVQKc2gCvgM,
             workers=50,
             sleep_threshold=10)

print("Developer: @pandaznetwork , Join & Share Channel")
print("Bot is Started Now")

@bot.on_message(filters.command('start') & filters.private)
async def start(client, message):
    btn = [[
        InlineKeyboardButton('Updates Channel', url=https://t.me/vikfy_official),
        InlineKeyboardButton('Support Group', url=https://t.me/vikfy_support)
    ],[
        InlineKeyboardButton('Deploy', url='https://github.com/pandaznetwork/Adlinkflyshortnerbot')
    ]]
    text = """**Just send me link and get short link, You can also send multiple links seperated by a space or enter."""
    await message.reply(f"👋 Hello {message.from_user.mention},\n\nI'm {vikfy} Shortner bot. {text}", reply_markup=InlineKeyboardMarkup(btn))    

@bot.on_message(filters.regex(r'https?://[^\s]+') & filters.private)
async def link_handler(bot, message):
    links = [match.group(0) for match in message.matches]

    processing_message = await message.reply("Processing your links...")

    try:
        short_links = await get_bulk_shortlinks(links)
        replaced_text = message.text
        for orig_link, short_link in zip(links, short_links):
            replaced_text = replaced_text.replace(orig_link, short_link)
        await bot.send_message(message.chat.id, replaced_text)
    except Exception as e:
        await message.reply(f'Error: {e}', quote=True)
    finally:
        await processing_message.delete()

async def get_bulk_shortlinks(links):
    short_links = []
    for link in links:
        short_link = await get_shortlink(link)
        short_links.append(short_link)
    return short_links

async def get_shortlink(link):
    params = {'api': API_KEY, 'url': link}

    async with aiohttp.ClientSession() as session:
        async with session.get(API_URL, params=params, raise_for_status=True) as response:
            data = await response.json()
            return data["shortenedUrl"]

       
bot.run()
