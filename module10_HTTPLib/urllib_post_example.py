import urllib.request
import urllib.parse

def send_post():
    url = "https://httpbin.org/post"
    data = {"name": "Niranjana", "role": "Trainer"}

    encoded_data = urllib.parse.urlencode(data).encode("utf-8")
    req = urllib.request.Request(url, data=encoded_data, method="POST")

    response = urllib.request.urlopen(req)
    print("POST Response:")
    print(response.read().decode("utf-8"))


if __name__ == "__main__":
    send_post()
