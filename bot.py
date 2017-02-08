import discord
import asyncio

class bot():
    def __init__(self):
        self.client = DiscordClient

    @client.event
    async def on_ready():
        print('Logged in as')
        print(client.user.name)
        print(client.user.id)
        print('------')
