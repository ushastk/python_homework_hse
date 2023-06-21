from bs4 import BeautifulSoup
import requests

authors = []
i = 1
while True:
    URL = f'https://quotes.toscrape.com/page/{i}/'
    response = requests.get(URL)
    soup = BeautifulSoup(response.content, 'html.parser')

    s = soup.find_all('span', class_='text')
    for el in s:
      quote = el.text
      author = el.find_next('small', class_='author').text
      if not(author in authors):
        authors.append(author);

    if soup.find('li', class_='next') == None:
        break
    i += 1

print('Количество страниц на сайте:', i)
print( 'Количество авторов на сайте:', len(authors))