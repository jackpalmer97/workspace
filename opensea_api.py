import requests

url = "https://api.opensea.io/api/v1/assets"
querystring = {"order_direction": "desc", "offset": "0", "limit": "20"}
response = requests.request("GET", url, params=querystring)

print(response.text)
