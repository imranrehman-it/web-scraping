from urllib import request
from bs4 import BeautifulSoup
import requests

url = "https://www.newegg.ca/p/pl?N=100007708%204814%20601292088%20601292090&cm_sp=Cat_video-Cards_2-_-Visnav-_-Full-Size-Video-Cards_1"

result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")
print(doc.prettify())
