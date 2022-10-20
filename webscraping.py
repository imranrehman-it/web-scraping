from urllib import request
from bs4 import BeautifulSoup
import requests

url = "https://globalnews.ca/tag/canadian-parliament/"

result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")
# print(doc.prettify())
urlList = []
for a in doc.find_all('a', href=True, ):
    if (a['href'].find('/news') != -1):
        print("Found the URL:", a['href'])
        urlList.append(a['href'])


subResult = requests.get(urlList[0])
subDoc = BeautifulSoup(subResult.text, "html.parser")
print(subDoc.prettify())
