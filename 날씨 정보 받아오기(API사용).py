import requests
import json

api = "https://api.openweathermap.org/data/2.5/weather?lat=36.6372&lon=127.4897&appid=74d770c4512ed5c7d54786102a2701fe&units=metric"

result = requests.get(api)
print(result.text)

data = json.loads(result.text)
# print(type(data))
print(data["name"], "의 날씨입니다.")
print("날씨는",data["weather"][0]["main"],"입니다.")
print("현재온도",data["main"]["temp"])
print("체감온도",data["main"]["feels_like"])
print("최저온도",data["main"]["temp_min"])
print("최저온도",data["main"]["temp_max"])


 