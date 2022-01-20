import discord

client = discord.Client()

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('hello'):
        await message.channel.send('hello,I am a bot')

client.run('OTMzNjc5NTc0Njc0NDY0Nzk4.YelC3Q.mYNipSrFKwIQtPo5dKAPhpHIN54')