from urllib import request
from bs4 import BeautifulSoup
import requests


url = "https://www.cbc.ca/news/world"
result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")


def extract_article(url):
    subResult = requests.get(url)
    subDoc = BeautifulSoup(subResult.text, "html.parser")
    article = ""

    for a in subDoc.find_all('p', {"class": None}):
        # gets all <p> up until end of article denoted by Audience Relations
        if (a.text.find("Audience Relations, CBC") != -1):
            break
        else:
            article = article + a.text

    return article


# extracts all links to news article from home page to be later accessed for article extraction
urlList = []
for a in doc.find_all('a', href=True, ):
    if (a['href'].find('/news/world') != -1):
        print("Found the URL:", a['href'])
        urlList.append(a['href'])


def write_article(article):
    with open("articles.txt", 'w') as f:
        f.write(extract_article("https://www.cbc.ca" + urlList[4]) + "\n")
    f.close()


print(extract_article("https://www.cbc.ca" + urlList[4]))
