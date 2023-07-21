#!/usr/bin/env python
# -*- coding: utf-8 -*-
from dash import html,dcc,dash_table
import dash_daq as daq
import pandas as pd
import datetime
import logging


from resources.style import default_style_page
from resources.htmlCreate import HtmlCreate
from resources.conf import Conf

class page_home():
    def __init__(self,app):
        self.app = app
        self.htmlCreate = HtmlCreate(app)
  

    def get_layout(self):
        """
        Layout.extend((self.layout_description_website(), self.layout_how_use_website(),
        self.layout_for_display_board()))
        :return: The layout of the page.
        """
        logging.info('Start make layout of page_jeux')
        layout=[]
        try:
            layout.extend((self.layout_description_website(), self.layout_how_use_website(), self.layout_for_display_board()))

        except Exception as error:
            logging.error(f'in get_layout  page_jeux : {error}',exc_info=True)

        return layout

    def layout_description_website(self):
        """
        It returns a Div element with a className of 'page-home-description' and two children: a Div
        element with a className of 'title_of_part_page' and a P element with a className of
        'paragraphe_of_part_page'.
        :return: The layout of the description of the website
        """
        layout = html.Div(
            className='page-home-description',
            children=[
                html.Div(
                    className='title_of_part_page',
                    children='Bienvenu sur notre site internet',
                ),
                 html.P(
                    className='paragraphe_of_part_page',
                    children="""Ce site est un outil dédier aux jeux de sociétés. 
                                Il vous permet en quelque clic d'ajouter des jeux votre collection ou à votre liste de j'aime.
                                Vous pouvez également notez tout les jeux rencontré sur ce site web !
                                Grâce à cela nous pourrons vous offrir la possibilité de trouver de nouveau jeux.
                                ce site sera donc idéale pour trouver des cadeaux ou des nouveaux jeux vous correspondant !""",
                ),
            ]
        )
        return layout

    def layout_how_use_website(self):
        """
        It returns a div with a class of 'page-home-use-website' that contains three divs, each with a
        class of 'page_home_part_of_list_like', 'page_home_part_of_collection', and
        'page_home_part_of_more'. Each of those divs contains a div with a class of 'title_of_part_page'
        and a div with a class of 'page_home_of_list_like', 'page_home_add_board_in_collection', and
        'page_home_of_more'. Each of those divs contains a div with a class of 'block_color' and a div
        with a class of 'page_home_description_of_like', 'page_home_description_of_collection', and
        'page_home_description_of_more'.</code>
        
        
        
        I'm trying to
        :return: A Div
        """
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
        return html.Div(
            className='page-home-use-website',
            children=[

                html.Div(
                    className='title_of_part_page',
                    children='Utilisation du site',
                ),
                html.Div(

                    className='page_home_part_of_list_like',
                    children=[

                        html.Div(
                            className='title_of_part_page',
                            children="Liste de j'aime",
                        ),
                        
                        html.Div(
                            className='page_home_of_list_like',
                            children=[
                                self.layout_cercle_of_home('yellow'),
                                html.Div(
                                    className='block_color yellow',
                                    children = [

                                        self.htmlCreate.get_card_of_boardgame(0,'Mysterium','./front/app/assets/jeux/image/mysterium.jpg',list_mesure,forhome=True,forhomeheart=True,forhomecoll=False,forhomemore=False),
                                         html.Div(
                                            className='img_cursor heart_action',
                                            children = [
                                                html.Img(
                                                        className='cursor_img',
                                                        src= self.htmlCreate.get_img_encore_for_src(path='./front/app/assets/pages/accueil/jeux_gif/image/cursor.png'),
                                                        alt='cursor'
                                                    )
                                            ]
                                        )
                                    ]
                                ),
                                html.Div(
                                    className='page_home_description_of_like',
                                    children="""
                                        La liste des j'aime correspond à tous vos coups de coeurs, il vous permet de n’oublier aucun jeux que vous avez découvert et vous permettra de vous souvenir ceux qu’il vous faut absolument.
                                    """
                                ),
                            ]
                        )
                    ]
                ),
                html.Div(

                    className='page_home_part_of_collection',
                    children=[
                        html.Div(
                            className='title_of_part_page',
                            children='La collection',
                        ),
                        html.Div(
                            className='page_home_add_board_in_collection',
                            children=[
                                self.layout_cercle_of_home('red'),
                                html.Div(
                                    className='block_color red',
                                    children = [

                                        self.htmlCreate.get_card_of_boardgame(1,'Mysterium','./front/app/assets/jeux/image/mysterium.jpg',list_mesure,forhome=True,forhomeheart=False,forhomecoll=True,forhomemore=False),
                                         html.Div(
                                            className='img_cursor collection_action',
                                            children = [
                                                html.Img(
                                                        className='cursor_img',
                                                        src= self.htmlCreate.get_img_encore_for_src(path='./front/app/assets/pages/accueil/jeux_gif/image/cursor.png'),
                                                        alt='cursor'
                                                    )
                                            ]
                                        )
                                    ]
                                ),
                                html.Div(
                                    className='page_home_description_of_collection',
                                    children="""
                                        la collection correspond au jeux que vous posseder,
                                        il permet de définir les jeux qu'il ne faut pas vous proposer,
                                        et vous permet aussi d'avoir une liste exaustive de tous vos jeux !
                                    """
                                ),

                            ]
                        ),
                        

                       
                    ]
                ),
                
                html.Div(

                    className='page_home_part_of_more',
                    children=[

                        html.Div(
                            className='title_of_part_page',
                            children="Détails du jeux",
                        ),
                        
                        html.Div(
                            className='page_home_of_more',
                            children=[
                                self.layout_cercle_of_home('blue'),
                                html.Div(
                                    className='block_color blue',
                                    children = [

                                        self.htmlCreate.get_card_of_boardgame(2,'Mysterium','./front/app/assets/jeux/image/mysterium.jpg',list_mesure,forhome=True,forhomeheart=False,forhomecoll=False,forhomemore=True),
                                         html.Div(
                                            className='img_cursor more_action',
                                            children = [
                                                html.Img(
                                                        className='cursor_img',
                                                        src= self.htmlCreate.get_img_encore_for_src(path='./front/app/assets/pages/accueil/jeux_gif/image/cursor.png'),
                                                        alt='cursor'
                                                    )
                                            ]
                                        )
                                    ]
                                ),
                                html.Div(
                                    className='page_home_description_of_more',
                                    children="""
                                       Les détails du jeux de société permet d'acceder aux information tel que la description et la note.
                                    """
                                ),
                            ]
                        )
                    ]
                )
            ]
        )
      

    def layout_for_display_board(self):
        """
        It returns a div with an id of 'page-board-display' and a class of 'page-board-display'.
        :return: The return statement is returning the html.Div() object.
        """

        return html.Div(
            id = 'page-board-display',
            className='page-board-display',
        )



    def layout_cercle_of_home(self,color):
        """
        If the color is yellow or blue, return a list of divs with the class name cercle_home and the
        color, except for the divs at the specified indices, which are empty
        
        :param color: the color of the circle
        :return: A list of divs.
        """
        return html.Div(
            className=f'content_cercle_of_home {color}',

            children=[html.Div(className=f'cercle_home {color}')  if i in [1,2,3,4,5,6,7,8,9,18,27,36,45,54,63] else html.Div() for i in range(1,51) ] if color in ['yellow','blue'] else [html.Div(className=f'cercle_home {color}')  if i in [1,2,3,4,5,6,7,8,9,10,19,28,37,46,55,64] else html.Div() for i in range(1,41) ]
        )