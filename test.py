import requests
import json
import urllib2
import dateutil.parser
import datetime


json_data = {
	'token': 'b511672d3601017b6572a772190bc56f',
	'github': 'https://github.com/yahirb/Code2040'
}

url = 'http://challenge.code2040.org/api/register'
headers = {'content-type': 'application/json'}
requests.post(url, data=json.dumps(json_data), headers=headers)



#Part 2
json_data_token = {
	'token': 'b511672d3601017b6572a772190bc56f'
} 
get_string_url = 'http://challenge.code2040.org/api/reverse'
reverse_string_url = 'http://challenge.code2040.org/api/reverse/validate'
response = requests.post(get_string_url, data=json.dumps(json_data_token), headers=headers)
temp = response.text
temp2 = temp[::-1]
json_data = {
	'token': 'b511672d3601017b6572a772190bc56f',
	'string': temp2
} 
response = requests.post(reverse_string_url, data=json.dumps(json_data), headers=headers)



#----------------------------Part 3----------------------------#

step3_url = 'http://challenge.code2040.org/api/haystack'
step3_validate_url = 'http://challenge.code2040.org/api/haystack/validate'
response = requests.post(step3_url, data=json.dumps(json_data_token), headers=headers)
dictionary = json.loads(response.text) 
needle = dictionary['needle']
haystack = dictionary['haystack']
index = haystack.index(needle)
json_data = {
	'token': 'b511672d3601017b6572a772190bc56f',
	'needle': index
} 
response = requests.post(step3_validate_url, data=json.dumps(json_data_token), headers=headers)


#----------------------------Part 4----------------------------#
step4_recieving_url = 'http://challenge.code2040.org/api/prefix'
step4_response_url = 'http://challenge.code2040.org/api/prefix/validate'
response = requests.post(step4_recieving_url, data=json.dumps(json_data_token), headers=headers)
dictionary = json.loads(response.text) 
prefix = dictionary['prefix']
array = dictionary['array']
temp_array = []
for s in array :
	if not s.startswith(prefix):
		temp_array.append(s)
json_data = {
	'token': 'b511672d3601017b6572a772190bc56f',
	'array': temp_array
} 
response = requests.post(step4_response_url, data=json.dumps(json_data), headers=headers)

#----------------------------Part 5----------------------------#


step5_recieving_url = 'http://challenge.code2040.org/api/dating'
step5_response_url = 'http://challenge.code2040.org/api/dating/validate'
response = requests.post(step5_recieving_url, data=json.dumps(json_data_token), headers=headers)
dictionary = json.loads(response.text)
datestamp = dictionary['datestamp']
interval = dictionary['interval']
yourdate = dateutil.parser.parse(datestamp)
updated_date = yourdate + datetime.timedelta(0,interval)
formatted_date = updated_date.isoformat()

print datestamp
print yourdate
print updated_date
print formatted_date
temp = formatted_date[:-6]
temp = temp + "Z"
print temp



json_data = {
	'token': 'b511672d3601017b6572a772190bc56f',
	'datestamp': temp
} 
response = requests.post(step5_response_url, data=json.dumps(json_data), headers=headers)

print response














""" NOTES FOR SELF
json.loads will load a json object into a python dict, 
json.dumps will dump a python dict to a json object 
"""
