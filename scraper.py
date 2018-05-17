import requests
from bs4 import BeautifulSoup
from io import StringIO
import json
from pprint import pprint

import operator
import bfConnector 
import drawClass


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
eventDict = dict()

#print(fixtures['fixtures'])
for fixture in fixtures['fixtures'] :
	
	
	homeTeam = fixture['home_team']
	awayTeam = fixture['away_team']
	number = fixture['number']
		
	print( fixture['home_team'] + '\tv\t' + fixture['away_team'] )	
	event = bfConnector.getEvent(homeTeam, awayTeam)
	
	
	
	if not event :
		notFoundList.append(  fixture['home_team'] + " v " + fixture['away_team'] + ", ")
					
	else :
		eventList.append(event)
		
		eventDict.update( { event[1] : drawClass.Draw(number, fixture['home_team'] + ' v ' + fixture['away_team'] ) } )

#print(str(eventDict))
print('Not Found List :')	
print(notFoundList)
'''
#print(eventList)
eventList = [['28696124', 'Chelsea v Man Utd'], ['28722665', 'Bayern Munich v Eintracht Frankfurt']]
'''

print('getting draw score odds ')

scoreDrawObjects = bfConnector.getScoreDrawOdds(eventList)
matchOddsObjects = bfConnector.getMatchOdds(eventList)


count = 0
for m in scoreDrawObjects :
	
	count += 1
	lookup = eventDict.get(m.name) 
	lookup.scoreOdds = count
	

count = 0
for m in matchOddsObjects :

	count += 1	
	lookup = eventDict.get(m.name) 
	lookup.matchOdds = count
	lookup.totalOdds = lookup.matchOdds + lookup.scoreOdds


print('Full Results')
for event in (sorted(eventDict.values(), key=operator.attrgetter('totalOdds'))):
	print(event)
	

print('\nTop 10 by scoreOdds')
count = 0
for event in (sorted(eventDict.values(), key=operator.attrgetter('scoreOdds'))):
	#print(event)
	print(str(event.id) + '\t:\t' + str(event.scoreOdds) + '\t:\t' + event.name )
	count += 1
	if count == 10 :
		break
	
print('\nTop 10 by matchOdds')
count = 0
for event in (sorted(eventDict.values(), key=operator.attrgetter('matchOdds'))):
	print(str(event.id) + '\t:\t' + str(event.matchOdds) + '\t:\t' + event.name )
	count += 1
	if count == 10 :
		break
	
print('\nTop 10 by totalOdds')
count = 0
for event in (sorted(eventDict.values(), key=operator.attrgetter('totalOdds'))):
	print(str(event.id) + '\t:\t' + str(event.totalOdds) + '\t:\t' + event.name )
	count += 1
	if count == 10 :
		break
