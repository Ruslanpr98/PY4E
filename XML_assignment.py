
import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

url = 'http://py4e-data.dr-chuck.net/comments_588543.xml'
print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read()
# if len(data) < 1:
#     break
print('Retrieved', len(data), 'characters')
print(data.decode())
tree = ET.fromstring(data)
trash = tree.findall('comments/comment')
lst_digits = list()
for item in trash:
    count = item.find('count').text
    count = int(count)
    lst_digits.append(count)
print(sum(lst_digits))

