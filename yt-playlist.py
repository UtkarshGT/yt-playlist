import requests
from bs4 import BeautifulSoup as soup
from pathlib import Path

my_url = "" # Put Youtube Playlist URL inside Quotes

# headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0"}

page_html = requests.get(my_url)
page_soup = soup(page_html.text, "lxml")

containers = page_soup.findAll("td",{"class":"pl-video-title"})

print("There are Total", len(containers), "videos in Playlist\n")

unavailable = []

for container in containers:
    title = container.text.replace("Channel name goes here","").strip() # Put Channel name

    file_name = Path(title + ".mp4")
    if file_name.is_file():
        continue
    else:
        unavailable.append(title)

print("Unavailable files are :\n")
for temp in unavailable:
    print(temp)
