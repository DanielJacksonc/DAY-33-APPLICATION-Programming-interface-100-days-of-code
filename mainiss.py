import time
import requests
from datetime import datetime
import smtplib

MY_LAT = 31.968599  # Your latitude
MY_LONG = -99.901810  # Your longitude
my_email = "pythondanielpython@gmail.com"
passwords = "sjrmiwoqvnxixlbi"


def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 or MY_LONG-5 <= iss_longitude <= MY_LONG:
        return True
    # Your position is within +5 or -5 degrees of the ISS position.


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    # If the ISS is close to my current position
    if time_now >= sunset or time_now <= sunrise:
        return True

    # and it is currently dark
    # Then send me an email to tell me to look up.
while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=passwords)
            connection.sendmail(
                from_addr=my_email,
                to_addrs="arcdaniel20@gmail.com",
                msg="Subject: THE ISS IS HERE!:\n\n hey, the ISS is over your house, do you want to check it out?")



# BONUS: run the code every 60 seconds.





