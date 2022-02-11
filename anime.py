import requests
from bs4 import BeautifulSoup

# passing the url for parsing the data through soup
url = 'https://9anime.vc/filter?keyword=&type=&status=all&season=&language=&sort=default&year=&genre='   
html = requests.get(url)
soup = BeautifulSoup(html.text, "html.parser")

# using the soup library to do futher processing (same as before)
# tags = soup.find_all('div', class_='movies_show')
# print(tags)
# tags = soup.find_all('li')
# for tag in tags:
#     a = tag.find('a')
#     print(a.get_text())
# ulst = tag.find_all('ul')
# print(ulst)
# lst = ulst[0].find_all('li')
# print(lst)
tags = soup.find_all('div',class_="film_list-wrap")
for tag in tags:
    a=tag.find('div',class_="flw-item item-qtip")
    b=a.get('h3')
    print(b)



  

print(tags)
# tags = tags[0].find_all('li')
# for tag in tags:
#     print(tag.get_text())