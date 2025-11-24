import requests

def fetch_weather():
    url = "https://wttr.in/London?format=j1"

    response = requests.get(url)
    data = response.json()

    current_temp = data["current_condition"][0]["temp_C"]
    print("Current Temperature in London:", current_temp, "°C")

if __name__ == "__main__":
    fetch_weather()
