# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input('Enter - ')
count = int(input("Enter count:"))
pos = int(input("Enter Position:"))-1
html = urllib.request.urlopen(url).read()

soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
href = soup('a')

for k in range(count):
    link = href[pos].get('href', None)
    found_url = urllib.request.urlopen(link).read()
    soup = BeautifulSoup(found_url,"html.parser")
    href = soup('a')
    print(href[pos].contents[0])