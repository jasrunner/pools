import requests
from bs4 import BeautifulSoup
from io import StringIO
import json
from pprint import pprint

import bfConnector 

'''
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

notFoundList = []

#fixtures = json.loads('{ "fixtures": [{"home_team": "Inter Milan", "away_team": "Sassuolo"}]}')

eventList = []

for fixture in fixtures['fixtures'] :
	
	
	homeTeam = fixture['home_team']
	awayTeam = fixture['away_team']
		
	print( fixture['home_team'] + '\tv\t' + fixture['away_team'] )	
	event = bfConnector.getEvent(homeTeam, awayTeam)
	
	eventList.append(event)
	
	if not event :
		notFoundList.append( "'"+ fixture['home_team'] + "' : " + fixture['away_team'] + "' ', ")
					
	else :
		print('\tevent Id :\tevent name')
		print('\t' + event[0] + '\t' + event[1])

print('Not Found List :')	
print(notFoundList)
'''
eventList = []
eventList.append([ ('28694906', 'Burnley v Bournemouth')])

print('getting draw score odds for ' + str(eventList[0]))
#bfConnector.getScoreDrawOdds(eventList)
bfConnector.getScoreDrawOdds(eventList[0])
