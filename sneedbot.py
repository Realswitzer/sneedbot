import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='@sneedbot#7364 ')
token = 'YOUR_TOKEN_HERE'


@bot.event
async def on_ready():
    print("In the wise words of sneed, blessed is the man who seeds, who \
allows others to feed. And let us who follow Sneed, forgive the city \
slickers who fear those who possess the 4 of clubs. They are lost \
and instead follow the degenerate path of chuck, and his globohomo \
tendencies.")


@bot.event
async def on_message(message):
    print(message)
    if 'sneed' in message.content.lower():
        await message.add_reaction(":sneedcube:945303603319537705")
    if '1984' in message.content:
        await message.add_reaction(":1984:945410219339554856")
    elif '1985' in message.content:
        await message.add_reaction(":1984:945410219339554856")
    elif '1986' in message.content:
        await message.add_reaction(":1984:945410219339554856")
    elif '1987' in message.content:
        await message.add_reaction(":1984:945410219339554856")
    elif '1988' in message.content:
        await message.add_reaction(":1984:945410219339554856")
    elif '1989' in message.content:
        await message.add_reaction(":1984:945410219339554856")
    elif '2001' in message.content:
        await message.add_reaction(":1984:945410219339554856")
    elif '1408' in message.content:
        await message.add_reaction(":1984:945410219339554856")


@bot.command()
async def sneed(ctx):
    await ctx.send("https://static.wikia.nocookie.net/simpsons/images/1/14/Al_ \
Sneed.png/revision/latest?cb=20210430000431")

bot.run(token)
