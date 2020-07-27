import json
import urllib.request, urllib.parse, urllib.error

url = 'http://py4e-data.dr-chuck.net/comments_588544.json'
data = urllib.request.urlopen(url)
read_data = data.read()

info = json.loads(read_data)
#print(info)
lst_of_dgts = list()
for item in info['comments']:
    lst_of_dgts.append(item['count'])
print(sum(lst_of_dgts))
