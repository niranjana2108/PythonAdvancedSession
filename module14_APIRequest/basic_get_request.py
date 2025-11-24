import requests

def get_google_homepage():
    url = "https://www.google.com"

    response = requests.get(url)
    print("Status Code:", response.status_code)
    print("Content Snippet:", response.text[:200])  # print first 200 chars

if __name__ == "__main__":
    get_google_homepage()
