import requests
from bs4 import BeautifulSoup

result = requests.get("https://www.google.com/")

src = result.content

soup = BeautifulSoup(src, 'html.parser')

links = soup.find_all("a")

for link in links:
    if link.text == "About Google":
        print(link.attrs["href"])
