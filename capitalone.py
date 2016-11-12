from rapidconnect import RapidConnect
import requests
import json

def coordinates(address):
	rapid = RapidConnect('FinanceBot', 'de800779-fee6-4bc8-ac71-0c239d9264f5');

	result = rapid.call('GoogleGeocodingAPI', 'addressToCoordinates', { 
		'apiKey': 'AIzaSyBQxQDQ5WEpn2hO9W5UaTD0iJe5xvaEsy0',
		'address': address
	});

	return result;

def find_atms(lat, lng, rad):
	url = 'http://api.reimaginebanking.com/atms'
	apiKey = '22827101aa2aed5f76342f276b3e38fb'
	payload = {   
	    "lat": lat,
	    "lng": lng,
	    "accessibility": True,
	    "rad": 1,
	    "key": apiKey
	  }
	r = requests.get(url, params = payload)
	arr = r.json()[u'data']
	for dic in arr:
		dic['dist'] = (dic[u'geocode'][u'lat'] - lat)**2 + (dic[u'geocode'][u'lng'] - lng)**2
	sort = sorted(arr, key=lambda dic: dic['dist'])
	return sort


def main():
	debug = 1;
	if debug == 1:
		address = '6930 Old Dominion Dr, McLean, VA 22101'
	else:
		address = raw_input("Enter an address: ")

	coords = coordinates(address)
	atms = find_atms(coords['lat'], coords['lng'], raw_input("Enter the radius: "))
	#for atm in atms:
	#	print atm['dist'], atm[u'_id'], '(', atm[u'geocode'][u'lat'], ', ', atm[u'geocode'][u'lng'], ')'
	
	best_atm = atms[0]
	address = best_atm[u'address']
	location = "%s %s, %s %s %s" % (address[u'street_number'], address[u'street_name'], address[u'city'],\
	 address[u'state'], address[u'zip'], )

	print location
main()
	