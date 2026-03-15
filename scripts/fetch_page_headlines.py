import requests
from bs4 import BeautifulSoup

url = "https://24h.com.vn"
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')

    headlines = soup.find_all('h2')

    for headline in headlines:
        print(headline.text)

else:
    print(f"Failed to retrive the page. Status code: {response.status_code}")
