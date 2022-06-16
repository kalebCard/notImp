fom  import Beautifulsoup
import request
import pandas as pd

url = https://www.metacritic.com/browse/games/score/metascore/year/all/filtered
page = request.get (url)
soup = Beautifulsoup(page.content, 'html.parser')

#Equipos

eq= soup.find_all('a', class_="title")


juegos = list()

for it in eq:
  equipos.append(i.text)
  
  print(equipos)
  
