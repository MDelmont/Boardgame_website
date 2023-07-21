#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pydoc import classname
from re import L
from dash import html,dcc,dash_table
import dash_daq as daq
import pandas as pd
import datetime
import logging


from resources.style import default_style_page
from resources.htmlCreate import HtmlCreate
from resources.conf import Conf

class page_jeux():
    def __init__(self,app):
        """
        It creates an instance of the Conf class, and assigns it to the variable self.conf
        
        :param app: The name of the application
        """
        self.conf = Conf()
        self.app = app
        self.htmlcreate = HtmlCreate(app)
  

    def get_layout(self):
        """
        Layout.extend((self.layout_for_display_board(), self.layout_for_filter_board()))
        :return: The layout of the page.
        """
        logging.info('Start make layout of page_jeux')
        layout=[]
        try:
            layout.extend((self.layout_for_display_board(), self.layout_for_filter_board()))
        except Exception as error:
            logging.error(f'in get_layout  page_jeux : {error}',exc_info=True)

        return layout

    def layout_for_filter_board(self):
        """
        It returns a Div element with a bunch of other elements inside it
        :return: The layout is being returned.
        """

        layout = html.Div(
            className='page-board-filter',
            children=[

                html.Div(
                    className='title_of_part_page',
                    children='Filtre des jeux',
                ),
                html.Div(
                    className='finder_with_name',
                    children=[
                        
                        dcc.Input(
                            className='finder_with_name_input'
                        ),
                        html.Img(
                            className='loupe_img',
                            src= self.htmlcreate.get_img_encore_for_src(path='./front/app/assets/pages/page_jeux/images/loupe.png'),
                            alt='loupe'
                        ),
                    ]
                ),
                html.Div(
                    id='see_filter_jeux',
                    className='see_filter',
                    children=self.make_icon_see_filter()


                ),

                html.Div(

                    className='part_of_filter',
                    children=[
                        self.make_case_filter_drop('theme'),
                        self.make_case_filter_drop('mecanique'),
                        html.Button(className='Appliquer_filter_play',children='Appliquer')
                    
                    ]

                )
            
            ]
        )
        return layout
    def make_case_filter_drop(self,name):
        """
        It takes a string as an argument and returns a Div with a paragraph and a dropdown
        
        :param name: the name of the case
        :return: A Div with a className of case_of_form.
        """

        return html.Div(
            className='case_of_form',
            children=[

                html.Div(
                    className='text_of_case_of_form',

                    children=html.P(
                            className='text_of_case',
                            children=name
                        ),
                ),
                
                dcc.Dropdown(
       
                    className='dropdown_of_make_case',
                    options=[{'label':i,'value':i} for i in ['test','test1','test2']],
                    multi=True,

                )
            ]
        )

    def layout_for_display_board(self):
        """
        It creates a list of cards, each card is a game, and each game is a list of players and their
        scores
        :return: The layout is being returned.
        """
        # sourcery skip: inline-immediately-returned-variable

        
                    
        layout = html.Div(
            id = 'page-board-display',
            className='page-board-display',
            children=[    self.htmlcreate.get_card_of_boardgame(i,play[0],play[1],self.conf.list_mesure) for i,play in enumerate(self.conf.list_demo_jeux)]
            
        )
        return layout


    def make_icon_see_filter(self):
        """
        It creates a div with three divs inside it
        :return: A Div element with className 'content_icon_see_filter' and three Div elements as
        children.
        """
        return html.Div(
            
            className='content_icon_see_filter',
            children=[
                html.Div(className= 'barre_1'),
                html.Div(className= 'barre_2'),
                html.Div(className= 'barre_3'),
            ]
        )