import requests

endpoint = '/boardgame_theme/add'


theme = {'id_boardgame':1,'id_theme':1}
r = requests.post(f'http://127.0.0.1:5000/{endpoint}',json=theme)


print(r.status_code)
print(r.text)