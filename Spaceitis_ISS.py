import json
import turtle
import urllib.request

url = 'http://api.open-notify.org/astros.json'   #URL of people who are in ISS in space
response = urllib.request.urlopen(url)           #Reading from the URL
result = json.loads(response.read())             #Converting from JSON to Python
print('People in space:',result['number'])       #Number of people in space

people = result['people']

for astro in people:                             #Printing names of people in space
  print(astro['name'], 'in ISS')

url = 'http://api.open-notify.org/iss-now.json'  #URL of live location of ISS and guess what! It travels at a speed of 7.66Km/hr#                                                 
response = urllib.request.urlopen(url)
result = json.loads(response.read())
location = result['iss_position']
lati=location['latitude']                        #Its latitude (yes, live latitude)
longi=location['longitude']                      #Its longitude (Ya,ya this too is live)
print('Latitude :',lati)
print('Longitude :',longi)
