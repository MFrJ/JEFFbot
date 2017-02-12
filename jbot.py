import asyncio
import discord
import re
from os import path

client = discord.Client()
command = re.compile("!([a-zA-Z0-9])+")
macro_dict = {}
with open("C:\\Users\\Marcelo\\Desktop\\JEFFbot\\resources\\txts\\macros.txt",'r') as f:
    if path.getsize("C:\\Users\\Marcelo\\Desktop\\JEFFbot\\resources\\txts\\macros.txt") > 0:
        for lines in f:
            if lines != "":
                (k,v) = lines.split(" ", 1)
                macro_dict[k] = v




def isMe(msg):
    return msg.author == client.user

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if not isMe(message):
        if message.content.startswith('!jeff'):
            await client.send_message(message.channel, "My nama jeff", tts=True)
        #macro list
        elif message.content.startswith('!memes'):
            with  open("C:\\Users\\Marcelo\\Desktop\\JEFFbot\\resources\\txts\\macros.txt",'r') as f:
                for lines in f:
                    (k,v) = lines.split(" ", 1)
                    await client.send_message(message.channel, k + ": " + v)
        #create macro            
        elif message.content.startswith("!"):
            if command.match(message.content):
                if command.match(message.content).group(0)[1:] in macro_dict.keys():
                    await client.send_message(message.channel, macro_dict[command.match(message.content).group(0)[1:]],tts=True)
                elif re.sub(command, "", message.content) != "":
                     macro_dict[command.match(message.content).group(0)[1:]] = re.sub("!([a-zA-Z0-9])+ ", "", message.content);
                     with open("C:\\Users\\Marcelo\\Desktop\\JEFFbot\\resources\\txts\\macros.txt",'a') as f:
                         f.write(command.match(message.content).group(0)[1:] + " " + macro_dict[command.match(message.content).group(0)[1:]].replace("\n"," ") + "\n")
                else:
                    await client.send_message(message.channel, "uso: !macro <txt>")
        elif command.search(message.content):
            if command.search(message.content).group(0)[1:] in macro_dict.keys():
                await client.send_message(message.channel, macro_dict[command.search(message.content).group(0)[1:]])





client.run("Mjc4ODYzMTA3NzU2MTMwMzA0.C3y1Ig.oKNoMuPhV0EUuC5TreOgBM8yUUo")
