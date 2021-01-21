import discord                                             # Импортируем библиотеку
from discord.ext import commands               # Импортируем из фреймворка класс commands

import config
import photo
import change_img

bot = commands.Bot(command_prefix='!')   # Провозглашаем переменную для бота с префиксом !

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')


@bot.event
async def on_message(message):
    msg = message.content.lower()
    name = message.author.name
    print(name, msg)

    if config.OVERLAY_PHOTO[0] in msg:
        await message.channel.send('Проверка...')
        url = msg[27:len(msg) + 1:1]
        photo.run(url)
        await message.channel.send('Обработка...')
        change_img.overlay_photo(config.PNAME)
        await message.channel.send(file=discord.File(config.PNAME))



bot.run(config.TOKEN)