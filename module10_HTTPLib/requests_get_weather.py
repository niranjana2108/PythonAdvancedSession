import requests

def fetch_weather():
    city = "India"
    api_url = f"https://wttr.in/{city}?format=j1"   # free weather API

    response = requests.get(api_url)

    if response.status_code == 200:
        data = response.json()
        temp = data["current_condition"][0]["temp_C"]

        print(f"Current Temperature in {city}: {temp}°C")
    else:
        print("Error fetching weather data")


if __name__ == "__main__":
    fetch_weather()
