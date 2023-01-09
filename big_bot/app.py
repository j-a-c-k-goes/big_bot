''' Core Imports '''
import os 
import discord
from dotenv import load_dotenv
import random
import datetime

''' Class Imports '''
from ResponseType import Affirmation

''' Server Setup '''
load_dotenv()
TOKEN = os.getenv( 'BOT_TOKEN' ) 
SERVER = os.getenv( 'SERVER_ID' )
TEST_CHANNEL = os.getenv( 'TEST_CHANNEL' )
BOT_NAME = os.getenv( 'BOT_NAME' )

''' Client Instances '''
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client( intents=intents )

@client.event
async def on_ready():
	''' Bot is ready. '''
	message = f'''!BIG is going to W3BBIE'''
	print( SERVER, message )

@client.event
async def on_message( message ):
	''' Message in channel '''
	response = Affirmation()
	trigger_string = '!BIGBIGBIG'.upper() or '!Big'
	notification_string = ( ( '!big'.lower() ) or ( '!big'.upper() ) or ( '!big'.title() ) )
	if message.author == client.user:
		return

	if message.content == trigger_string:
		await message.reply( content= f'`update:` { response.positive() }' )
		await message.reply( content=f'@{ message.author.display_name} does it !big {event.emoji*random_number() }')
	if message.content in notification_string:
		await message.reply(content= response.positive())

	if (message.content == 'BIG') or (message.content == 'big') or (message.content =='Big'):
		await message.reply(content= f'`update:` { response.forgetting_punctuation() }' )
	else:
		return

@client.event
async def on_disconnect():
	''' !big was disconnected '''
	print(f'{ BOT_NAME } booting down. see you next time.')
client.run(TOKEN)