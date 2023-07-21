#!/usr/bin/env python
# -*- coding: utf-8 -*-
import dash_bootstrap_components as dbc
from dash import html, dcc
from resources.htmlCreate import HtmlCreate
class Header():
    def __init__(self,app):
        htmlcreate=  HtmlCreate(app)
        self.menu =html.Div(
            className='menu',

            children=[

                    html.Div(
                        className='navigation_mobil',
                        children=[

                            html.Ul(
                                children=[
                                    *[htmlcreate.get_list_for_header(id=part[0], li_class_name=part[1],path_of_img=part[2],name_of_part=part[3]) for part in [
                                                ['list-1','active','./front/app/assets/menu/icons/home.png','Accueil'],
                                                ['list-2','','./front/app/assets/menu/icons/list.png','Ma liste'],
                                                ['list-3','','./front/app/assets/menu/icons/jeux.png','Jeux'],
                                                ['list-4','','./front/app/assets/menu/icons/find.png','Suggestion'],
                                                ['list-5','','./front/app/assets/menu/icons/profil.png','Profil']  ]],htmlcreate.get_pieces_html()


                                 
                                    ]
                                ),

                        ],
                    ),

                 
                    html.Ul(
                        className='navigation_web',
                        children=[
                            *[htmlcreate.get_card_for_header(color=card[0],
                                                            name=card[1],
                                                            path_img_color=card[2],
                                                            path_img_white=card[3],
                                                            path_img_black=card[4],
                                                            number_card=card[5]) for card in [[ 'purple',
                                                                                                'Accueil',
                                                                                                './front/app/assets/menu/icons/chess_purple.png',
                                                                                                './front/app/assets/menu/icons/chess_white.png',
                                                                                                './front/app/assets/menu/icons/chess.png',
                                                                                                1],
                                                                                                [ 'yellow',
                                                                                                'Ma liste',
                                                                                                './front/app/assets/menu/icons/list_yellow.png',
                                                                                                './front/app/assets/menu/icons/list_white.png',
                                                                                                './front/app/assets/menu/icons/list.png',
                                                                                                2],
                                                                                                [ 'green',
                                                                                                'Jeux',
                                                                                                './front/app/assets/menu/icons/jeux_green.png',
                                                                                                './front/app/assets/menu/icons/jeux_white.png',
                                                                                                './front/app/assets/menu/icons/jeux.png',
                                                                                                3],
                                                                                                [ 'red',
                                                                                                'Suggestion',
                                                                                                './front/app/assets/menu/icons/find_red.png',
                                                                                                './front/app/assets/menu/icons/find_white.png',
                                                                                                './front/app/assets/menu/icons/find.png',
                                                                                                4],
                                                                                                [ 'blue',
                                                                                                'Profil',
                                                                                                './front/app/assets/menu/icons/profil_blue.png',
                                                                                                './front/app/assets/menu/icons/profil_white.png',
                                                                                                './front/app/assets/menu/icons/profil.png',
                                                                                                5]]]
                            ]
                        ),

                    
              
                    
        
        
        ],)

        
