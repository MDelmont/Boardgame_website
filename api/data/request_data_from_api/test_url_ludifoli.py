from bs4 import BeautifulSoup
import requests
import json
url_scrap_possible : f'https://www.philibertnet.com/fr/50-jeux-de-societe/s-3/langue-francais/categorie-jeux_classiques+jeux_de_cartes+jeux_enfants+jeux_de_figurines+jeux_d_histoire+jeux_de_role+jeux_de_societe?p={i}&orderby=sales&orderway=desc'
url_list = []
for i in range(1,178):
    url = f'https://www.ludifolie.com/10-jeux-societe-adulte?page={i}'
    print(url)

    response = requests.get(url)

    print(response.status_code)
    soup = BeautifulSoup(response.text,'html.parser')

    list_jeux_url = soup.find_all('a',{'class':'thumbnail product-thumbnail'})

    for jeux in list_jeux_url:
        url_list.append(jeux['href'])

print(len(url_list))
f = open('list_url','a')
f.write(json.dumps({'jeux':url_list}))
f.close()


