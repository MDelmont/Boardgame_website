#!/usr/bin/env python
# -*- coding: utf-8 -*-

from socketserver import ThreadingUDPServer
from dash import html,dcc
from dash.dependencies import Input, Output
from app import App
from resources.htmlCreate import HtmlCreate
from pages.header import Header
from pages.page_jeux import page_jeux
from pages.page_home import page_home
from resources.htmlCreate import HtmlCreate
from callbacks import callback

application = App()
app = application.app
server = application.server
header = Header(app)
session_id = ''
list_mesure =[    { 'class':'info_board_age',
                                'value':'8',
                                'unite':'ages',
                            },
                            {
                                'class':'info_board_nbplayers',
                                'value':'2-5',
                                'unite':'joueurs',
                            },
                            {
                                'class':'info_board_minutes',
                                'value':'30-45',
                                'unite':'minutes',
                            }]
description = """Mysterium est un jeu d’enquête coopératif dans lequel tous les joueurs sont unis dans un même but\xa0: découvrir la vérité sur la mort du fantôme qui hante le manoir et lui apporter la paix !"""

dict_atrib = {
    'Thème':['Fanstastique'],
    'Mécanique':['Amérique','Enigme','Moyen-Orient']
}
callback.import_all_callback(app)
#layout rendu par l'application
app.layout = html.Div(id='page',
    children=[
        dcc.Location(id='url', refresh=True),
        html.Div(session_id, id='session-id'),
        
        html.Div(id='page-content',
        children =page_home(app).get_layout()),
        
        header.menu,
        html.Div(
            id='boardgame_big',
            className='boardgame_big',
            children = HtmlCreate(app).get_big_card_of_boardgame(0,'mysterium','./front/app/assets/jeux/image/mysterium.jpg',list_mesure,description,dict_atrib),
        ),
        HtmlCreate(app).get_layout_for_personne_not_connect()
    ])

# def generate_variables(app):
#     page_jeu = page_jeux(app)
#     page_h = page_home(app)
#     return page_jeu, page_h

# page_jeu, page_h = generate_variables(app)

# endpoints = {
#          '/': page_h.get_layout(),
#         }

#callback pour mettre à jour les pages
# @app.callback(Output('page-content', 'children'),
#               [Input('url', 'pathname')])
# def display_page(pathname):
#     try:
#         return endpoints[pathname]
#     except Exception as error:
#         return f"ERROR : {error}"

if __name__ == '__main__':
    app.run_server(debug=True)