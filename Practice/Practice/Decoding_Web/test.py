import requests

url = 'http://github.com'
r = requests.get(url)
r_html = r.text