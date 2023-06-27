import requests
import json

def weatherTemp():
    print("--------- WELCOME ---------\n")
    city = input("Enter city name:")

    url = f"https://api.weatherapi.com/v1/current.json?key=70d9f075f5cb4fa8b2b113745232706&q={city}&aqi=no" # url got from api dashboard 

    r = requests.get(url)

    wDic = json.loads(r.text)

    temp = wDic["current"]["temp_c"]
    print(f"Temperature in {city} is {temp} degree celcius")

weatherTemp()