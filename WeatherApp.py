import requests

API_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxx" 

"""You may get Your own API key, just by registering at :https://openweathermap.org
The url is taken from the API doc. at 'https://openweathermap.org/api' """

BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

city = input("Please Enter a City Name: ")

request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
'''This line is constructing a URL using f-string.Here, ‘?’ is a
special character and is used to start the query string portion
of a URL. A ‘query string’ is typically used to pass key-value pairs 
to the server. In this case, two pairs are passed: ‘appid’ and ‘q’. 
Whareas ‘&’ is another character which is used to separate 
multiple key-value pairs in a URLs query string. After the 
first key-value pair, you want to include another, so you use ‘&’'''

response = requests.get(request_url)

"""HTTP status codes are three-digit numbers that provide a quick way
for the client to understand the result of their request to a server.
e.g.; 200:OK, 404:Not Found, 502:Bad Gateway etc""" 

if response.status_code == 200:
    data = response.json()
    
    print("................................................")
    weather_data = data['weather'][0]['description'] # Using key to access value
    temperature_data = round(data['main']['temp'] - 273.15,2) # Using keys 'main' & 'temp' to access values
    print(f"The Weather of {city} : {weather_data}")
    print(f"The Temperature of {city} : {temperature_data} Degree Celsius ")
    print("................................................")
    
    # print(data) # To display the JSON form of data
    
else:
    print("An error occurred.")