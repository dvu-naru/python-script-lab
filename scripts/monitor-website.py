import requests

url = "https://bongda.com.vn"
response = requests.get(url)

try :
    if response.status_code == 200:
        print("Website is up!")
    else:
        print("Website is down!")
except Exception as e:
    print("Website is not working!")