import requests

def parse_weather_details():
    url = "https://wttr.in/Chennai?format=j1"

    response = requests.get(url)
    weather_json = response.json()

    print("=== PARSED WEATHER DETAILS ===")
    print("Temperature:", weather_json["current_condition"][0]["temp_C"])
    print("Humidity:", weather_json["current_condition"][0]["humidity"])
    print("Weather Description:", weather_json["current_condition"][0]["weatherDesc"][0]["value"])

if __name__ == "__main__":
    parse_weather_details()
