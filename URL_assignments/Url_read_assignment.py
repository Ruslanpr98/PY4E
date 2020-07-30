
from urllib.request import urlopen
from bs4 import BeautifulSoup

url = input('Enter - ')
html = urlopen(url).read()
soup = BeautifulSoup(html, "html.parser")
list_of_nums = list()
# Retrieve all of the anchor tags
tags = soup('span')
for tag in tags:
    # Look at the parts of a tag
    print(tag)
    print(tag.contents[0])
    digit = tag.contents[0]
    digit = int(digit)
    list_of_nums.append(digit)
print(sum(list_of_nums))