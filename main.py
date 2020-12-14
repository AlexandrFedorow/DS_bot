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
    file = open('data.txt', 'a')
    msg = message.content.lower()
    name = message.author.name

    file.write(name + ' ' + msg + '\n')
    file.close()
    print(name, msg)

    if config.PICTURE_CGANGE[0] in msg:  # обработка пикчи нужно все протестить
        await message.channel.send('Проверка...')
        try:
            url = msg[20:len(msg) + 1:1]
            photo.run(url)
            await message.channel.send('Обработка...')
            change_img.chenge1(config.PNAME)
            await message.channel.send(file=discord.File(config.PNAME))

        except:
            await message.channel.send('ОШИБКА')

    elif config.OVERLAY_PHOTO[0] in msg:
        await message.channel.send('Проверка...')
        try:
            url = msg[27:len(msg) + 1:1]
            photo.run(url)
            await message.channel.send('Обработка...')
            change_img.overlay_photo(config.PNAME)
            await message.channel.send(file=discord.File(config.PNAME))

        except:
            await message.channel.send('ОШИБКА')


bot.run(config.TOKEN)                    # Запускаем бота с вашим токеном