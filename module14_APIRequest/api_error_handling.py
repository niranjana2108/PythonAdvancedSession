import requests

def safe_api_call():
    url = "https://jsonplaceholder.typicode.com/posts/1"

    try:
        response = requests.get(url, timeout=5)

        if response.status_code == 200:
            print("Success!")
            print(response.json())
        else:
            print(f"Error: Received status code {response.status_code}")

    except requests.exceptions.Timeout:
        print("Error: Request timed out")

    except requests.exceptions.ConnectionError:
        print("Error: No internet connection or server down")

if __name__ == "__main__":
    safe_api_call()
