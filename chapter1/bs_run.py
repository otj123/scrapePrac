from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://www.pythonscraping.com/pages/page1.html')
bs = BeautifulSoup(html.read(), 'html.parser')
bs1 = BeautifulSoup(html, 'html.parser')
print('html의 값')
print(html)
print('html의 자료형')
print(type(html))
print('html.read()의 값')
print(html.read())
print('html.read()의 자료형')
print(type(html.read()))
print('bs의 값')
print(bs)
print('bs1의 값')
print(bs1)
print('bs의 자료형')
print(type(bs))
print("="*100)

bs2 = BeautifulSoup(html.read(), 'lxml')
print(bs2)
print(type(bs2))

bs3 = BeautifulSoup(html.read(), 'html5lib')
print(bs3)
print(type(bs3))
