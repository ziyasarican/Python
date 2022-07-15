import requests
from bs4 import BeautifulSoup

url = "https://www.trendyol.com/bluetooth-kulaklik-x-c108626"

html = requests.get(url).content
soup = BeautifulSoup(html,"html.parser")

list = soup.find_all("div",{"class":"p-card-wrppr"})

temp=1
for span in list:
    name = span.find("span",{"class":"prdct-desc-cntnr-name hasRatings"}).text
    price = span.find("div",{"class":"prc-box-dscntd"}).text
    print(temp,name,price)
    temp+=1
