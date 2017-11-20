import requests
import BeautifulSoup

url = 'http://www.nytimes.com/'
ttl_lst = []

soup = BeautifulSoup.BeautifulSoup(requests.get(url).text)
title = soup.findAll('h2', {'class': 'story-heading'})
for row in title:
     ttl_lst.append(row.text)

print ttl_lst