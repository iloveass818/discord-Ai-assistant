import discord
from discord import Message, Intents, Client
from typing import Final
import os
import dotenv
from responses import get_response

import responses

intents: Intents = Intents.default()
intents.message_content = True
client: Client = Client(intents=intents)

async def send_message(message: Message, user_message: str) ->None:
    if not user_message:
        print('(message was empty because intents werent setup properly')
        return
    if is_private := user_message[0] == '?':
        user_message=user_message[1:]

    try:
        response:str = get_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)




def run_discord_bot():
    TOKEN = 'MTIzMDU1NzQ2Njk3MDgyMDc0MA.GyR_h5.JJvj7I7CeqJczc7tZodcs9snlCFB2klb9QCZB8'

    @client.event
    async def on_ready():
        print(f'{client.user} is ready.')

    @client.event
    async def on_message(message: Message) -> None:
        if message.author == client.user:
            return

        username: str = str(message.author)
        user_message: str = str(message.content)
        channel: str = str(message.channel)

        print(f'[{channel}] {username}: "{user_message}"')
        await send_message(message, user_message)


    client.run(TOKEN)
