import requests
import json

API_KEY = "e73957290c0f398b138f3ef3880dda77"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?q="
city = input('Introdu numele orasului:')
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
rasp = requests.get(request_url)
data = json.loads(rasp.text)
print(data)
