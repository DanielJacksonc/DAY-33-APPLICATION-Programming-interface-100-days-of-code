import requests
from _datetime import  datetime

MY_LAT = 37.090240
MY_LNG = -95.712891

parameters = {
 "lat": MY_LAT,
 "lng": MY_LNG,
 "formatted": 0


 }
response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
# We raise an exception for the response
response.raise_for_status()
data = response.json()

# We split our data into sunrise and sunset
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

"""we want to know the time in our local, we will need  use the datetime module"""
today = datetime.now()
now = today.time()
print(sunrise)
print(sunset)
print(now.hour)