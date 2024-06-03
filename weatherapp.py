import requests

city= "Mumbai"
API_Key='cd28ed1c86894701abebf21dcdc112b0'
url=f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_Key}& units=metric'

response=requests.get(url)
if response.status_code==200:
    data=response.json()
    print(city)
    print("weather is",data['weather'] [0]['description'] )
    print ("current temperature is",data['main']['temp'])
    print ("current pressure is",data['main']['pressure'])
    print("current humidity is",data['main']['humidity'])
    print("current speed of wind is",data['wind']['speed'])
