import discord
from configparser import ConfigParser

config_parser = ConfigParser()
config_parser.read('config.ini')
token = config_parser['discord']['token']
text_channel_name = config_parser['discord']['channel']

client = discord.Client()

@client.event
async def on_ready():
  print('Connected!')
  print('Username: ' + client.user.name)
  print('ID: ' + client.user.id)

@client.event
async def on_message(message):
  if (message.channel.name == text_channel_name and message.author != client.user):
    msg = await client.send_message(message.channel, 'valid message')


client.run(token)