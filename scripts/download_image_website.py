import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

URL = input("Please input to download images: ")
SAVE_FOLDER = input("Please input folder: ")

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/121.0.0.0 Safari/537.36"
    ),
    "Accept-Language": "en-US,en;q=0.9",
}


def download_images(url):
	if not os.path.exists(SAVE_FOLDER):
		os.mkdir(SAVE_FOLDER)

	print(f"[+] Fetching page {url}")
	response = requests.get(url, headers=HEADERS)
	response.raise_for_status()

	soup = BeautifulSoup(response.text, "html.parser")

	img_tags = soup.find_all("img")
	print(f"[+] Found {len(img_tags)} images.")

	for img in img_tags:
		img_url = img.get('src')

		if not img_url:
			continue

		img_url = urljoin(url, img_url)

		filename = os.path.join(SAVE_FOLDER, img_url.split("/")[-1].split('?')[0])
		filename = filename.replace("\x00", "")

		try:
			print(f"   - Downloading: {img_url}")
			img_data = requests.get(img_url).content

			with open(filename, "wb") as f:
				f.write(img_data)


		except Exception as e:
			print(f"   - Filed to download {filename}: {e}")

# Run the function
download_images(URL) 
