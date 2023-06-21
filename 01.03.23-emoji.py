from bs4 import BeautifulSoup
import requests
url = 'https://emojipedia.org/search/'
categories = ["nature", "music", "science"]
emojis = []
n = 0
for category in categories:
  params = {'q': category}
  response = requests.get(url, params = params)
  soup = BeautifulSoup(response.text, 'html.parser')
  ol = soup.find('ol', class_='search-results')
  li_all = ol.find_all('li')
  for li in li_all:
    name = li.find('a')
    description = li.find('p')
    emojis.append( ( name.text, description.text ) )
    n +=1
  print("В категории", category, "-", n, "эмоджей:")
  for item in emojis:
    print("   ", item[0], '=', item[1])
  n = 0
  emojis = []