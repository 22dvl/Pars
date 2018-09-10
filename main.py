from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup

urladr = "http://www.pythonscraping.com/pages/page1.html"

def getTitle(url):
    try:
        ohtml = urlopen(url)                        # Открываем заданную страницу
    except HTTPError:
        return None
    except URLError:
        return None
    try:
        html = ohtml.read()                         # Передаем в переменную HTML код страницы
        head = BeautifulSoup(html, 'html.parser')   # Преобразование HTML кода в структуру BS4
        title = head.body.h1                        # Извлечение заголовка
    except AttributeError:
        return None
    return title

title = getTitle(urladr)
if title is None:
    print("Title could not be found")
else:
    print(title)