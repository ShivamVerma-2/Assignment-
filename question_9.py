import requests


city = "Delhi"
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=7dfa18947cdd023b693b06b75e027cb2&units=metric"

response = requests.get(url)
data = response.json()

if response.status_code == 200:
    weather = {
        "City": city,
        "Temperature (°C)": data["main"]["temp"],
        "Humidity (%)": data["main"]["humidity"],
        "Weather": data["weather"][0]["description"],
        "Wind Speed (m/s)": data["wind"]["speed"]
    }

    for key, value in weather.items():
        print(f"{key}: {value}")
else:
    print("Error fetching data:", data.get("message", "Unknown error"))
