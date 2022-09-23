import requests

# print(requests.__version__)

# print(requests.get("http://google.com"))

response = requests.get("https://raw.githubusercontent.com/DaY-w/CMPUT-404-lab-1/master/get.py")
print(response.content)