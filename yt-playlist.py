from bs4 import BeautifulSoup as soup
import requests

my_url = "" # Enter Youtube Playlst URL inside Quotes

# headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0"}

page_html = requests.get(my_url)
page_soup = soup(page_html.text, "lxml")

containers = page_soup.findAll("td",{"class":"pl-video-title"})

print("There are Total", len(containers), "videos in Playlist")

unavailable = []

for container in containers:
    title = container.text.replace("by sentdex","").strip()

    try:
        open((title + ".mp4"), "r")
        
    except:
        unavailable.append(title)

print(unavailable)