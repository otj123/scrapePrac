from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen('http://www.pythonscraping.com/pages/page3.html')
bs = BeautifulSoup(html, 'html.parser')

lam1 = bs.find_all(lambda tag: len(tag.attrs) == 2)

lam2 = bs.find_all(lambda tag: tag.get_text() == 'Or maybe he\'s only resting?')
lam3 = bs.find_all('', text='Or maybe he\'s only resting?')

print(lam1)
print(lam2)
print(lam3)