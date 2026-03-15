import requests
import os
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import json

URL = input("Website Url to crawl: ")
FILE = input("Json filename: ")

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121 Safari/537.36"
}

def scrape_posts(url):
    posts = []

    r = requests.get(url, headers=HEADERS)
    r.raise_for_status()

    soup = BeautifulSoup(r.text, "html.parser")

    # Common selectors for articles/posts
    candidates = soup.select("article, .post, .card, .news-item, .item, .post-item, li, .entry")

    for c in candidates:
        title = None
        link = None
        brief = None
        img = None

        # Title
        title_tag = c.find(["h1", "h2", "h3", "h4", "a"])
        if title_tag:
            title = title_tag.get_text(strip=True)

        # Link
        link_tag = c.find("a")
        if link_tag and link_tag.get("href"):
            link = urljoin(url, link_tag.get("href"))

        # Brief
        brief_tag = c.find("p")
        if brief_tag:
            brief = brief_tag.get_text(strip=True)

        # Image
        img_tag = c.find("img")
        if img_tag and img_tag.get("src"):
            img = urljoin(url, img_tag.get("src"))

        # Only append if title & link exist
        if title and link:
            posts.append({
                "title": title,
                "brief": brief,
                "link": link,
                "image": img
            })

    return posts


# Fetch all posts
posts = scrape_posts(URL)

print(json.dumps(posts, indent=4, ensure_ascii=False))

folder = os.path.dirname(FILE)

# Validate filed exists 
# Create a new file if it is not exists
if not os.path.exists(folder):
	os.makedirs(folder)

# Save to file folder
with open(FILE, "w", encoding="utf-8") as f:
	json.dump(posts, f, indent=4, ensure_ascii=False)

print("\nSaved to json")