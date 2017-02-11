import asyncio
import discord
import re

client = discord.Client()
macro_dict = {}
command = re.compile("!([a-zA-Z0-9])+")

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
        elif message.content.startswith("!"):
            if command.match(message.content):
                if command.match(message.content).group(0)[1:] in macro_dict.keys():
                    await client.send_message(message.channel, macro_dict[command.match(message.content).group(0)[1:]])
                elif re.sub(command, "", message.content) != "":
                     macro_dict[command.match(message.content).group(0)[1:]] = re.sub("!([a-zA-Z0-9])+ ", "", message.content);
                else:
                    await client.send_message(message.channel, "uso: !macro <txt>")
        elif command.search(message.content):
            if command.search(message.content).group(0)[1:] in macro_dict.keys():
                await client.send_message(message.channel, macro_dict[command.search(message.content).group(0)[1:]])

        # if message.content.startswith('!test'):
        #     counter = 0
        #     tmp = await client.send_message(message.channel, 'Calculating messages...')
        #     async for log in client.logs_from(message.channel, limit=100):
        #         if log.author == message.author:
        #             counter += 1
        #
        #     await client.edit_message(tmp, 'You have {} messages.'.format(counter))
        # elif message.content.startswith('!sleep'):
        #     await asyncio.sleep(5)
        #     await client.send_message(message.channel, 'Done sleeping')



client.run("Mjc4ODYzMTA3NzU2MTMwMzA0.C3y1Ig.oKNoMuPhV0EUuC5TreOgBM8yUUo")
