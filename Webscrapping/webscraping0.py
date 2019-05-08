from bs4 import BeautifulSoup
import pandas as pd 
import requests
url=requests.get("https://www.fifauteam.com/fifa-19-ligue-1-midfielders-guide/").text
soup = BeautifulSoup(url,'lxml')
#print(soup.prettify())
name_box = soup.find("table", attrs={"class": "tableizer-table"})

df=pd.read_html(str(name_box))