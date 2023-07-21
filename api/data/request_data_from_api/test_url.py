

from bs4 import BeautifulSoup
import requests

url_scrap_possible : 'https://www.philibertnet.com/fr/50-jeux-de-societe/s-3/langue-francais/categorie-jeux_classiques+jeux_de_cartes+jeux_enfants+jeux_de_figurines+jeux_d_histoire+jeux_de_role+jeux_de_societe?orderby=sales&orderway=desc'
url = 'https://boardgamegeek.com/xmlapi2/thing?parameters&id=[,316554,3]&type=boardgame&stats=1'


response = requests.get(url)

print(response.status_code)
soup = BeautifulSoup(response.text,'lxml')

boardgames = soup.find_all('item',{'type':'boardgame'})

print(len(boardgames))

for boardgame in boardgames:
    print("name is :", boardgame.find('name',{'type':'primary'})['value'])
    print("     image is :", boardgame.find('image').text)
    print("     yearpublished is :", boardgame.find('yearpublished')['value'])
    print("     minplayers is :", boardgame.find('minplayers')['value'])
    print("     maxplayers is :", boardgame.find('maxplayers')['value'])
    print("     minplaytime is :", boardgame.find('minplaytime')['value'])
    print("     maxplaytime is :", boardgame.find('maxplaytime')['value'])
    print("     minage is :", boardgame.find('minage')['value'])
    print("     description is :",boardgame.find('description').text[0:10])
    print("     family list is :", [family['name'] for family in  boardgame.find_all('rank',{'type':'family'})])
    print("     categorie list is :", [family['value'] for family in  boardgame.find_all('link',{'type':'boardgamecategory'})])
    print("     mechanic list is :", [family['value'] for family in  boardgame.find_all('link',{'type':'boardgamemechanic'})])
    print("     designer is :", boardgame.find('link',{'type':'boardgamedesigner'})['value'])


        