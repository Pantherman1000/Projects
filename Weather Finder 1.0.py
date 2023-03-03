import urllib.request, urllib.parse, urllib.error
import json


print("Welcome to the Adi's Weather App!")
begin = input('Please type "Start" to begin:\n')
while begin.lower() in ["start", "yes", "y"]:
    city = input("Please enter your city:\n")
    serv_url = 'http://api.openweathermap.org/geo/1.0/direct?'
    final_url = serv_url + urllib.parse.urlencode({
        'q': city, 
        'limit': 1, 
        'appid': '2055d2b375ea0abe219910e1944b2d3b'
    })

    try:
        geo = urllib.request.urlopen(final_url)
        data1 = geo.read().decode()
        info1 = json.loads(data1)
        if info1:
            lat_raw = info1[0]['lat']
            lon_raw = info1[0]['lon']
            lat = None
            lon = None
            if lat_raw > 0:
                lat = f'{lat_raw}{chr(176)}N'
            elif lat_raw < 0:
                lat = f'{lat_raw*-1}{chr(176)}S'
            if lon_raw > 0:
                lon = f'{lon_raw}{chr(176)}E'
            elif lon_raw < 0:
                lon = f'{lon_raw*-1}{chr(176)}W'
            print(f'Latitude {lat}')
            print(f'Longitude {lon}')
        else:
            print("No results found.")

    except urllib.error.URLError as e:
                print("Error:", e.reason)
    except json.JSONDecodeError as e:
            print("Error: Invalid JSON response")

    weather = input("Would you like to see the weather conditions for your area?\n")
    if weather.lower() in ["yes", "y"]:
        service_url = 'https://api.openweathermap.org/data/2.5/weather?'
        url = service_url + urllib.parse.urlencode({
            'lat': lat_raw, 
            'lon': lon_raw, 
            'appid': '2055d2b375ea0abe219910e1944b2d3b', 
            'units': 'metric', 
            'lang' : 'en'
        })

        try:
            file = urllib.request.urlopen(url)
            data = file.read().decode()
            info = json.loads(data)
            if info:
                weather = info["weather"][0]["description"]
                avg_temp = info["main"]["temp"]
                apparent_temp = info["main"]["feels_like"]
                min_temp = info["main"]["temp_min"]
                max_temp = info["main"]["temp_max"]
                pressure = info["main"]["pressure"]
                humidity = info["main"]["humidity"]
                visibility = info["visibility"]
                wind_speed = info["wind"]["speed"]
                print(f'Conditions over {city}:')
                print(f'Weather Conditions: {weather.title()}')
                print(f'Average Temperature: {round(avg_temp, 1)}{chr(176)}C')
                print(f'Feels Like: {round(apparent_temp, 1)}{chr(176)}C')
                print(f'Minimum Temperature: {round(min_temp, 1)}{chr(176)}C')
                print(f'Maximum Temperature: {round(max_temp, 1)}{chr(176)}C')
                print(f'Pressure: {round(pressure, 1)}hPa')
                print(f'Humidity: {round(humidity, 1)}%')
                print(f'Visibility: {round(visibility, 1)}km')
                print(f'Wind Speed: {round(wind_speed*3.6, 1)}km/hr')
                begin = input("Would you like to continue using this program?\n")
        except urllib.error.URLError as e:
            print("Error:", e.reason)
        except json.JSONDecodeError as e:
            print("Error: Invalid JSON response")
    elif weather.lower() in ["no", "n"]:
         begin = input("Would you like to continue using this program?\n")
print("Thank You for using this program!")