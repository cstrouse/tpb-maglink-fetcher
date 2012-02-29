from bs4 import BeautifulSoup
import requests
import sys

#order_by = 7=seeders, 9=leachers, 5=size, 1=name, 3=uploaded, 11=uploader

url = "http://thepiratebay.se/search/%s/0/7/0" % (sys.argv[1])

# TODO: Use magnet_links to write a tool for auto downloading the first result of each run
#magnet_links = []

soup = BeautifulSoup(requests.get(url).content)
results = soup.find_all('a', {'class': 'detLink'})
for result in results:
    torrent = {}
    torrent['title'] = result.string
    torrent['magnet_link'] = soup.find('a', attrs={'title': 'Download this torrent using magnet'})['href']
    print torrent['title']
    print torrent['magnet_link']
    print
    #magnet_links.append(torrent)
    
