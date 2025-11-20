import urllib.request

def fetch_example():
    url = "https://httpbin.org/get"
    response = urllib.request.urlopen(url)
    data = response.read().decode("utf-8")

    print("GET Response:")
    print(data)


if __name__ == "__main__":
    fetch_example()
