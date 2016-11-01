import requests
api_key = "b511672d3601017b6572a772190bc56f"
response = requests.get('http://challenge.code2040.org/api/register')

print response.body