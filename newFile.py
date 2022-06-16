fom  import Beautifulsoup
import request
import pandas as pd

url = https://www.metacritic.com/browse/games/score/metascore/year/all/filtered
page = request.get (url)
soup = Beautifulsoup(page.content, 'html.parser')

#Equipo

