import discord
import requests
import json
import asyncio


client = discord.Client()

@client.event
def get_question():
    qs = ''
    id = 1
    answer = 0
    response = requests.get("https://mysterious-fjord-93163.herokuapp.com/api/random/")
    json_data = json.loads(response.text)
    qs += "Question: \n"
    qs += json_data[0]['title'] + "\n"

    for item in json_data[0]['answer']:
        qs += str(id) + ". " + item['answer'] + "\n"

        if item['is_correct']:
            answer = id

        id += 1

    return (qs, answer)


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$question'):

        qs, answer = get_question()
        await message.channel.send(qs)

        def check(m):
            return m.author == message.author and m.content.isdigit()

        try:
            guess = await client.wait_for('message', check=check, timeout=2.0)
        except asyncio.TimeoutError:
            return await message.channel.send('Za długo ByczQ')

        if int(guess.content) == answer:
            await message.channel.send('Masz racje!')
        else:
            await message.channel.send('Oops. nie tym razem')

client.run('')
