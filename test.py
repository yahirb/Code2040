import requests
import json
import urllib2

json_data =  {
	'token': 'b511672d3601017b6572a772190bc56f',
	'github': 'https://github.com/yahirb/Code2040'
} 

url = 'http://challenge.code2040.org/api/register'
headers = {'content-type': 'application/json'}

response = requests.post(url, data=json.dumps(json_data), headers=headers)

print response