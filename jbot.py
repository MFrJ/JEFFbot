import asyncio
import discord

client = discord.Client()

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
    if message.content.startswith('!macro'):
        s = message.content[7:]
        if (',') not in s:
            await client.send_message(message.channel, "!macro: <key>,<txt>")
        else :
            l = s.split(",")
            await client.send_message(message.channel, ">".join(l))
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
    elif message.content.startswith('!jeff'):
        await client.send_message(message.channel, "My nama jeff", tts=True)


client.run("Mjc4ODYzMTA3NzU2MTMwMzA0.C3y1Ig.oKNoMuPhV0EUuC5TreOgBM8yUUo")
