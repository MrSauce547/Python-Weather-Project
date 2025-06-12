import requests

api_key = '387222d2bcc5398ad1660812cd28695f'

user_input = input("Enter city: ")

weather_data = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")

weather = weather_data.json()['weather'][0]['main']
temp = weather_data.json()['main']['temp']
feels_like = weather_data.json()['main']['feels_like']
temp_min = weather_data.json()['main']['temp_min']
temp_max = weather_data.json()['main']['temp_max']
country = weather_data.json()['sys']['country']

temp_added = temp_max + temp_min
temp_avg = temp_added // 2

print(f"{user_input}'s weather today:")
print("Sky:", weather, "|", "Temperature:", round(
    temp), "|", "Feels like:", round(feels_like))
print("Maximum temp:", round(temp_max), "|", "Minimum temp:", round(temp_min))
print("Average temperature:", round(temp_avg))

if country != 'US':
    print("Country:", country)
