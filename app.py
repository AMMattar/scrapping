import requests
from bs4 import BeautifulSoup
import pandas as pd

headers = {'User-Agent':
           'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'}

page = "https://www.transfermarkt.com/egyptian-premier-league/transfers/wettbewerb/EGY1?saison_id=2020"
pageTree = requests.get(page, headers=headers)
pageSoup = BeautifulSoup(pageTree.content, 'html.parser')

Players = pageSoup.find_all(
    "a", {"class": "spielprofil_tooltip"})

# Let's look at the first name in the Players list.
# print(Players)
print(Players[0].text)

#Values = pageSoup.find_all("td", {"class": "rechts hauptlink"})

# fees / from / to / position
#goals / assists / yellow /red / plyrmatch / intplyr
#carlength / sqcarelegth / teamtenure / teamtrafee
# team league / club administration

#PlayersList = []
#ValuesList = []

# for i in range(0, 25):
#    PlayersList.append(Players[i].text)
#    ValuesList.append(Values[i].text)

#df = pd.DataFrame({"Players": PlayersList, "Values": ValuesList})

# df.head()
