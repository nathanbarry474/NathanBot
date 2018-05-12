#NathanBot by Nathan

import discord
import random
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import sys

client = discord.Client()

@client.event
async def on_ready():
    await client.change_presence(game = discord.Game(name = "Jada"))
    print('Logged in as ' + client.user.name)
    print('with the ID: ' + client.user.id)

@client.event
async def on_message(message):
    if message.author == client.user:
        return

#Emojis
    if message.content.startswith("Scott"):
        msg = "<:Scott:440301183941345281>".format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith("God"):
        msg = "<:krabs:441780976893427713>".format(message)
        await client.send_message(message.channel, msg)

#Dadbot
    if message.content.startswith("I'm"):
        msg = message.content.split()
        msg = msg[1:]
        msg = " ".join(msg)
        await client.send_message(message.channel, ("Hi %r I'm Nathan") % msg)

#Respond
    if message.content.startswith("Hey"):
        msg = "What's up {0.author.mention}".format(message)
        await client.send_message(message.channel, msg)
#Respond to Isaac
    print(message.author)
    if message.author == 'TIME#2485':
        await client.sent_message(message.channel, "this is isaac")

#Change Role
@client.event
async def on_member_join(member):
    role = discord.utils.get(member.server.roles, name = 'Jelqees Peasants')
    await client.add_roles(member, role)
        
client.run("NDMwNDEzNTgwNjUxNzI0ODAw.DaUk3w.QL6NdXLnjMr0wf2mXVIraluHmA8")