import telepot
import time
import requests
from bs4 import BeautifulSoup

token = 'Insert your token'
bot = telepot.Bot(token)

# First enter the name of singer with first letter of the name in capitals than write the song name.
# Example- Maroon 5 maps
def main(cmd):
	s = cmd['text']
	song = s.replace(' ', '-')
	response = requests.get('https://genius.com/'+song+'-lyrics')
	soup = BeautifulSoup(response.text, 'html.parser')
	tag = soup.find('p')
	lyrics = tag.text
	bot.sendMessage(cmd['chat']['id'], lyrics)

print('bot is listening')
bot.message_loop(main)

while True:
	time.sleep(10)
