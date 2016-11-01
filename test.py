import requests
import json
import urllib2

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



#Part 3
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


#Part 4
step4_recieving_url = 'http://challenge.code2040.org/api/prefix'
step4_response_url = 'http://challenge.code2040.org/api/prefix/validate'
response = requests.post(step4_recieving_url, data=json.dumps(json_data_token), headers=headers)
dictionary = json.loads(response.text) 
prefix = dictionary['prefix']
array = dictionary['array']
print array
print "\n"
temp_array = []
print "The prefix is: " + prefix
for s in array :
	if not s.startswith(prefix):
		temp_array.append(s)
print temp_array
print "\n"
json_data = {
	'token': 'b511672d3601017b6572a772190bc56f',
	'array': temp_array
} 

jsonarray = json.dumps(json_data)
print jsonarray
response = requests.post(step4_response_url, data=json.dumps(json_data), headers=headers)
print response






""" NOTES FOR SELF
json.loads will load a json object into a python dict, 
json.dumps will dump a python dict to a json object 
"""
