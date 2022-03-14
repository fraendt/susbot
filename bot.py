import asyncio
import logging
import discord
from discord.ext.commands import Bot
from discord.ext.commands.errors import MissingRequiredArgument
import os
from dotenv import load_dotenv

logging.basicConfig(level=logging.INFO)
load_dotenv()

client = Bot(command_prefix="!")

@client.command(name='embed', description='embed test', help='embed test')
async def embeded(ctx):
    embed=discord.Embed(title="top text",
                        description="bottom text",
                        color=0xFF5733)
    await ctx.send(embed=embed)

@client.command(name='echo', description='echo', help='echo')
async def echo(ctx, message=''):
    if message=='':
        return
    await ctx.send(message)

@client.command(name='where')
async def where(ctx):
    global w
    w=ctx
    await ctx.send(ctx.channel)


async def confirmation(ctx, message):
    m = await ctx.send(message)
    yn = ['✅', '🚫']
    for i in yn:
        await m.add_reaction(i)
    try:
        reaction = await ctx.bot.wait_for('raw_reaction_add', timeout=30,
                                          check=lambda r: r.user_id == ctx.message.author.id and str(r.emoji) in yn and r.message_id == m.id)
    except asyncio.TimeoutError:
        await ctx.send('Timed out.')
        return False
    else:
        if str(reaction.emoji) == yn[0]:
            return True
        else:
            return False
    finally:
        try:
            await m.delete()
        except:
            pass
    await ctx.send(reaction)
    m.delete()

@client.command(name='sus')
async def sus(ctx):
    global m
    m = await ctx.send('🤨📷')
    
    await asyncio.sleep(0.2)
    await m.edit(content='🤨📸')
    await asyncio.sleep(0.05)
    await m.edit(content='🤨📷')
    await asyncio.sleep(0.05)
    await m.edit(content='🤨📸')
    await asyncio.sleep(0.05)
    await m.edit(content='🤨📷')

@client.event
async def on_ready():
    logging.info("Ready")
    
client.run(os.getenv('LULW'))
