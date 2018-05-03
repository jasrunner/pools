import requests
from bs4 import BeautifulSoup
from io import StringIO
import json
from pprint import pprint


# *****************************************************
# the following code block is to scrape from a website 
theUrl = 'https://www.footballpools.com/pool-games/classic-pools'

# get the part of interest - not sure how constant this is week on week
# maybe shoukd find a better way of getting this.
r = requests.get(theUrl)
soup=BeautifulSoup(r.content, "html5lib")
script = soup.findAll('script')[4].string

# extract the last part based on square brackets
endBracket = script.rfind(']')
startBracket = script.rfind('[')
allFixtures = script[startBracket:endBracket+1]

# make it vaild json
allFixtures = '{ "fixtures": ' + allFixtures + '}'
#print(allFixtures)
fixtures = json.loads(allFixtures)


# *****************************************************
'''

with open('example_input.json') as json_data:
	fixtures = json.load(json_data)
'''

# *****************************************************

for fixture in fixtures['fixtures'] :
	print(fixture['home_team'])
#io = StringIO("example_input.json")
#json.loads(io)


