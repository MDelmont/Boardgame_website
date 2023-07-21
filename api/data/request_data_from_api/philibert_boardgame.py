import json
import requests
from bs4 import BeautifulSoup
import logging
path = "./api/data/data_brut/url/list_url_philibert.json"
contents={}
with open(path, 'r', encoding='utf-8') as j:
     contents = json.loads(j.read())['jeux']




logging.basicConfig(filename=f"outlogs.log",level=logging.DEBUG,format='%('levelname')-8s %(asctime)s %(message)s')


i = 0
for url in contents:
    logging.info(f'Stats n°{i}:')
    print(i)
    logging.info(f'   -> Url : {url}')
    boardgame = {}
    response = None
    try:
        response = requests.get(url)
        print('status code is ' ,response.status_code)
    except Exception as error:
        logging.error(f'   -> Error in request : {error} ')

    
    if response:
        soup = None
        try:
            soup = BeautifulSoup(response.text,'html.parser')
        except Exception as error:
            logging.error(f'Error in soup : {error}')
        
        if soup:
            name= None
            try:

                name = soup.find("h1",{"id":"product_name"}).text
                logging.info(f'   -> name : {name}')
            except Exception as error:
                logging.error(f'   -> in name : {error}')

            minage= None
            try:

                minage = soup.find("li",{"class":"age tooltips"}).text
                logging.info(f'   -> minage : {minage}')
            except Exception as error:
                logging.error(f'   -> in minage : {error}')

            duree= None
            try:

                duree = soup.find("li",{"class":"duree_partie tooltips"}).text
                logging.info(f'   -> duree : {duree}')
            except Exception as error:
                logging.error(f'   -> in duree : {error}')
            
   
            nb_joueur= None
            try:

                nb_joueur = soup.find("li",{"class":"nb_joueurs tooltips"}).text
                logging.info(f'   -> nb_joueur : {nb_joueur}')
            except Exception as error:
                logging.error(f'   -> in nb_joueur : {error}')

            description= None
            try:

                description = soup.find("section",{"id":"tab-description"}).text
                logging.info(f'   -> description : {description[0:25]}')
            except Exception as error:
                logging.error(f'   -> in description : {description}')

            little_description= None
            try:

                little_description = soup.find("div",{"id":"short_description_content"}).text
                logging.info(f'   -> little_description : {little_description[0:25]}')
            except Exception as error:
                logging.error(f'   -> in little_description : {little_description}')
   

            url_image= None
            try:

                url_image = soup.find("img",{"itemprop":"image"})["src"]
                logging.info(f'   -> url_image : {url_image[0:25]}')
            except Exception as error:
                logging.error(f'   -> in url_image : {url_image}')


            prix= None
            try:

                prix = soup.find("span",{"id":"our_price_display"}).text
                logging.info(f'   -> prix : {prix}')
            except Exception as error:
                logging.error(f'   -> in prix : {prix}')

            try:
                fiche_technique = soup.find("section",{"id":"tab-features"})
                caracteristique = fiche_technique.find_all('tr',{'class':['even']})
                caracteristique.extend(fiche_technique.find_all('tr',{'class':['odd']}))

                Theme = ''
                mecanique=''
                Auteur=''
                for lines in caracteristique:
                    detail = lines.find_all('td')
                    if detail[0].text == 'Thème(s)':
                        try:

                            Theme = detail[2].text
                            logging.info(f'   -> Theme : {Theme}')
                        except Exception as error:
                            logging.error(f'   -> in Theme : {Theme}')
             
                    if detail[0].text == 'Mécanisme(s)':
                        try:

                            mecanique = detail[2].text
                            logging.info(f'   -> meca : {mecanique}')
                        except Exception as error:
                            logging.error(f'   -> in meca : {mecanique}')
               
                    if detail[0].text == 'Auteur(s)':
                        try:

                            Auteur = detail[2].text
                            logging.info(f'   -> Auteur : {Auteur}')
                        except Exception as error:
                            logging.error(f'   -> in Auteur : {Auteur}')
              
            except Exception as error:
                logging.error(f'   -> in fiche technique : {prix}')
            

            


            boardgame['url'] = url
            boardgame['name'] = name
            boardgame['minage'] = minage
            boardgame['duree'] = duree
            boardgame['nb_joueur'] = nb_joueur
            boardgame['description'] = description
            boardgame['little_description'] = little_description
            boardgame['url_image'] = url_image
            boardgame['prix'] = prix
            boardgame['Theme'] = Theme
            boardgame['mecanique'] = mecanique
            boardgame['Auteur'] = Auteur


            path= f"E:\matth\Documents\Cours\Wild code school\Data Scientist\side-project\\boardgame\\api\data\data_brut\philibert\\boardergame{i}.json"
            data = json.dumps(boardgame, default=str)
            with open(path, 'a') as j:
                j.write(data)
            


    i+=1

