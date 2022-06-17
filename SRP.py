#import
from bs4 import BeautifulSoup
import requests
import pandas as pd
#variables
url=("loreimpus")
#urlGet
page=requests.get(url)
soup=BeautifulSoup(page.content,'html.parser')
#equipos:
eq=soup.find_all("loreimpus",class_="loreimpus")
equipos=list()
count=0
for i in eq:
  if count<20:
    equipos.append(i.text)
  else:
    break
  count +=1
#puntos
pt=soup.find_all("loreimpus",class_="loreimpus")
puntos=list()
count=0
for i in pt:
  if count<20:
    puntos.append(i.text)
  else:
    break
  count +=1
#csvSave
df = pd.DataFrame({'Nombre':equipos,'Puntos':puntos}, index=list(range(1,21)))
df.to_csv('Clasificacion.csv', index=False)
print("Lista CSV guardada")
print (df)
