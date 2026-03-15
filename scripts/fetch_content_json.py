import requests

url_file_json = "https://json-ld.org/contexts/person.jsonld"
req = requests.get(url_file_json)

data_json = req.json()

if '@context' in data_json:
    live_data = data_json
    print(f"current traffic data: {live_data}")
else:
    print("Data is not found in the API response")
