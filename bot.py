import discord

from bot_token import TOKEN

from discord.ext import commands

import chatbot

bot = commands.Bot(command_prefix='', description="Codeucate's Customer Service Bot")
@bot.event
async def on_ready():

    print('Logged in as')

    print(bot.user.name)

    print(bot.user.id)

    print('------')



@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    await message.channel.send(chatbot.return_response(message.content))

async def on_member_join(member):
    await member.send("Hello! I am ROBO, and I'll be there to answer any questions that you might have!")


bot.run(TOKEN)
