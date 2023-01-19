import requests
from bs4 import BeautifulSoup
import smtplib
from apscheduler.schedulers.blocking import BlockingScheduler
from hashlib import new

def data_scraping() :
    req=requests.get("https://www.emag.ro/telefon-mobil-apple-iphone-14-pro-max-128gb-5g-deep-purple-mq9t3rx-a/pd/DXDY4LMBM/?cmpid=99160&gclid=CjwKCAjw7p6aBhBiEiwA83fGutQEzd8jTFRrgGNgq-64rJSekVI_-HBUv2ljRnybUWvX7Ny_Rzh68hoClScQAvD_BwE")
    soup=BeautifulSoup(req.text,"html.parser")
    price=soup.find('p', attrs={'class': 'product-new-price'}).text
    new_price=price[0:5]
    new_price=new_price.replace(".","")
    print(new_price)

def trimitere_mail ():
    server = smtplib.SMTP('mail.x-it.ro', 26)
    server.starttls()
    server.login("data_scraping@coneasorin.ro"."stiinte217_2002")
    server.sendmail("data_scraping@coneasorin.ro","hirtescuandrei@gmail.com","UPDATE: AVEM O MODIFICARE DE PRET")
    print("Emailul a fost trimis cu succes")
    server.quit

#data_scraping()
trimitere_mail()
