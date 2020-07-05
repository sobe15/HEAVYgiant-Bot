import discord

client = discord.Client()

@client.event 
async def on_ready():
    print('We Have Iogged in as {0.user}'.format(client))

def method_name():
    return 'Hello!'

async def method_name(message):
    await message.channel.send(method_name())

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$강욱아'):
        await message.channel.send('왜! 뭐! 왜부르는데!!')

    if message.author == client.user:
        return

    if message.content.startswith('$야'):
        await message.channel.send('왜 무머머ㅓ머무머뭠뭐뭐뭐뭐뭐뭐뭐!!!!!!!')

    if message.author == client.user:
        return

    if message.content.startswith('$송'):
        await message.channel.send('강욱')

client.run('NzI1Mjc1MTQxMTUxNTIyODg4.XwFQiw.Hp0RqXUqOKIgMxto4MkoGeCmsvw')
