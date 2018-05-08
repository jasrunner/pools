import urllib
import urllib.request
import urllib.error
import sys


sys.path.insert(0, '../JasBFBotRepo')

import connectionDetails
import foxyBotLib
import strategy
import foxyGlobals
import mappings

appKey = connectionDetails.getDelayedKey()
sessionToken 	=  connectionDetails.getSessionId()


foxyGlobals.headers = {'X-Application': appKey, 'X-Authentication': sessionToken, 'content-type': 'application/json'}


def getEvent(homeTeam, awayTeam):
	
	event = strategy.getSetOfWeekendEvents( 'Soccer', homeTeam, awayTeam)
	
	if not event :
		event = strategy.getSetOfWeekendEvents( 'Soccer', homeTeam, awayTeam.split(None, 1)[0])
			
		if not event : 	
			event = strategy.getSetOfWeekendEvents( 'Soccer', homeTeam.split(None, 1)[0], awayTeam)
			
			if not event :
				event = strategy.getSetOfWeekendEvents( 'Soccer', homeTeam.split(None, 1)[0], awayTeam.split(None, 1)[0])
				
				if not event :
					if ' ' in awayTeam :
						event = strategy.getSetOfWeekendEvents( 'Soccer', homeTeam, awayTeam.split(None, 1)[1])
					
						if not event :
							if ' ' in homeTeam :
								event = strategy.getSetOfWeekendEvents( 'Soccer', homeTeam.split(None, 1)[1], 	awayTeam.split(None, 1)[1])		
		
					elif ' ' in homeTeam :
						event = strategy.getSetOfWeekendEvents( 'Soccer', homeTeam.split(None, 1)[1], awayTeam)
					
					# try mappings
					if not event :
						if mappings.TeamMapping.get(homeTeam) :
							event = strategy.getSetOfWeekendEvents( 'Soccer', mappings.TeamMapping.get(homeTeam), awayTeam)
							
							if not event :
								if mappings.TeamMapping.get(awayTeam) :
									event = strategy.getSetOfWeekendEvents( 'Soccer', mappings.TeamMapping.get(homeTeam), mappings.TeamMapping[awayTeam])
				
						elif mappings.TeamMapping.get(awayTeam) :
							event = strategy.getSetOfWeekendEvents( 'Soccer', homeTeam, mappings.TeamMapping[awayTeam])
							

	return event
	



