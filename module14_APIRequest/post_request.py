import requests

def create_post():
    url = "https://jsonplaceholder.typicode.com/posts"

    new_post = {
        "title": "Learning APIs in Python",
        "body": "This is a sample POST request",
        "userId": 1
    }

    response = requests.post(url, json=new_post)

    print("Status Code:", response.status_code)
    print("Response JSON:")
    print(response.json())

if __name__ == "__main__":
    create_post()
