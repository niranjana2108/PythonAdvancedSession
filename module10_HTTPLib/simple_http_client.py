import requests

def call_server():
    url = "http://localhost:8080"
    response = requests.get(url)
    print("Server response:")
    print(response.text)

if __name__ == "__main__":
    call_server()
