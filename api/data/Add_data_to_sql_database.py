from encodings.utf_8 import encode
import os
import json
import re
import requests
path = './api/data/data_brut/philibert/'
 
files = os.listdir(path)

#name_file = files[0:25]

for name_file in files:
    print(name_file)
    try:
        with open(f'{path}{name_file}', encoding='utf-8') as f:
            boardgame_brut =  json.load(f)

        boardgame = {}
        theme_board = []
        mecanic_board = []
        is_good_send = []
        for key,value in boardgame_brut.items():
    
            if key in ['name','description','little_description','url_image']:

                boardgame[key] = value
            if key =='url':
        
                boardgame['source_url'] = value
            if key =='minage':
                boardgame['minage'] = re.search(pattern='\d+|\d',string=value).group(0)  if 'à partir de' in str(value) else None
                boardgame['maxage'] = re.search(pattern='\d+|\d',string=value).group(0)  if 'moins de' in str(value) else None
            if key == 'duree':
                minplaytime = re.search(pattern='\d+|\d',string=value).group(0)  if 'et plus' in str(value) else None
                maxplaytime =  re.search(pattern='\d+|\d',string=value).group(0)  if 'moins de' in str(value) else None
                if 'à' in str(value):
                    minplaytime,maxplaytime = (re.findall(pattern='\d+|\d',string=value)[0] if value else None,re.findall(pattern='\d+|\d',string=value)[1]if value else None)
                boardgame['minplaytime'] = minplaytime
                boardgame['maxplaytime'] =maxplaytime
            if key =='nb_joueur':
            
                minplayers = re.search(pattern='\d+|\d',string=value).group(0)  if 'joueur' in str(value) else None
                maxplayers =  minplayers
                if 'à' in str(value):
                    minplayers,maxplayers = (re.findall(pattern='\d+|\d',string=value)[0],re.findall(pattern='\d+|\d',string=value)[1])
                boardgame['minplayers'] = minplayers
                boardgame['maxplayers'] =maxplayers

            if key == 'prix':
                boardgame['price'] = float(re.search(pattern='(\d,\d) €|(\d+,\d+) €|(\d,\d+) €|(\d+,\d) €',string=value).group(2).replace(',','.'))  if '€' in str(value) else None
            
            if key == 'Auteur':
                boardgame['designer'] =value
                
            

            if key == 'Theme':
                value = str(value).replace('\xa0','').replace('\n','').replace(' ','').replace(';',',')
                if value:
                    if not ',' in value and not value in theme_board:
                        theme_board.append(value)
                    else:
                        for val in value.split(','):
                            if  val not in theme_board:
                                theme_board.append(val)
            
            if key == 'mecanique':
                value = str(value).replace('\xa0','').replace('\n','').replace(' ','').replace(';',',')
                if value:
                    if not ',' in value and not value in mecanic_board:
                        mecanic_board.append(value)
                    else:
                        for val in value.split(','):
                            if  val not in mecanic_board:
                                mecanic_board.append(val)



        result = requests.post('http://127.0.0.1:5000/boardgame/add',json=boardgame)
        is_good_send.append(result.json()['is_send'])
        board_id = result.json()['id']

        for theme in theme_board:
            if theme:
                result = requests.post('http://127.0.0.1:5000/theme/add',json={'name':theme})
                theme_id = result.json()['id']
                is_good_send.append(result.json()['is_send'])
                board_theme = {
                    'id_boardgame' :board_id,
                    'id_theme' : theme_id,
                }

                requests.post('http://127.0.0.1:5000/boardgame_theme/add',json=board_theme)
                is_good_send.append(result.json()['is_send'])


        for meca in mecanic_board:
            if meca:
                result = requests.post('http://127.0.0.1:5000/mechanic/add',json={'name':meca})
                is_good_send.append(result.json()['is_send'])
                mecanique_id = result.json()['id']

                board_meca = {
                    'id_boardgame' :board_id,
                    'id_mechanic' : mecanique_id,
                }

                result = requests.post('http://127.0.0.1:5000/boardgame_mechanic/add',json=board_meca)
                is_good_send.append(result.json()['is_send'])
        
        print(is_good_send)
    except Exception as error:
        print(error)

   