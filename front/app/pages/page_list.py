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

class page_list():
    def __init__(self,app):
        """
        It creates an instance of the class Conf and HtmlCreate, and assigns them to the variables
        self.conf and self.htmlcreate
        
        :param app: The name of the application
        """
        self.app = app
        self.conf = Conf()
        self.htmlcreate = HtmlCreate(app)
  

    def get_layout(self):
        """
        Layout.append(self.layout_for_display_board())
        layout.append(html.Div(
                        className='side_page_stats_filter',
                        children = [
                            self.layout_for_filter_board(),
                            self.layout_for_stats_board(),
                        ]
                    ))
        :return: The layout of the page.
        """
        logging.info('Start make layout of page_list')
        layout=[]
        try:

            
            
            layout.append(self.layout_for_display_board())
            layout.append(html.Div(
                className='side_page_stats_filter',
                children = [
                    self.layout_for_filter_board(),
                    self.layout_for_stats_board(),
                ]
            ))
    


        except Exception as error:
            logging.error(f'in get_layout  page_list : {error}',exc_info=True)

        return html.Div(
            className='page_list',
            children=layout)
    def layout_for_stats_board(self):
        """
        It returns a div with two children, each of which is a function call to make_podium
        :return: A dictionary with the keys '1', '2', and '3' and the values 'Enigme', 'Tuille', and
        'Plateau'
        """
        return html.Div(
            className='page-board-stats',
            children=[
                self.make_podium('Top mécanique',{'1':'Enigme','2':'Tuille','3':'Plateau'}),
                self.make_podium('Top theme',{'1':'Fantastique','2':'Pirate','3':'Animaux'})
            ]

            )

    def make_podium(self,title,dict_placement_podium):
        """
        It creates a div with a title and three divs inside it, each with a title and a number. 
        
        The number is the key of the dictionary passed to the function, and the title is the value of
        the dictionary. 
        
        The order of the divs is determined by the order of the keys in the dictionary. 
        
        The class of the div with the number is determined by the value of the dictionary. 
        
        The class of the div with the title is always 'title_of_part'. 
        
        The class of the div with the number is always 'block_of_part'. 
        
        The class of the div with the title and the three divs inside it is always 'cont_part_podium'. 
        
        The class of the div with the title and the div with the three divs inside it is always '
        
        :param title: the title of the podium
        :param dict_placement_podium: a dictionary with the keys being the placement and the values
        being the name of the placement
        :return: A Div element with a className of 'cont_podium' and children of a Div element with a
        className of 'title_podium' and children of title, and a Div element with a className of
        'cont_part_podium' and children of a Div element with a className of 'part_podium' and children
        of a Div element with a className
        """
        return html.Div(
            className='cont_podium',
            children=[
                html.Div(
                    className='title_podium',
                    children=title
                ),
                html.Div(
                    className='cont_part_podium',
                    children=[

                        html.Div(
                            className='part_podium',
                            children=[
                                html.Div(
                                    className='title_of_part',
                                    children=dict_placement_podium[i],
                                ),
                                html.Div(
                                    className=f'block_of_part {name_class}',
                                    children=i
                                )
                            ]
                        ) for i, name_class in [('3','number_three'),('1','number_one'),('2','number_two')]
                    ]
                )
            ]
        )


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
                        self.make_case_filter_drop('Liste'),
                       
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
        :return: A Div element with a className of case_of_form.
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
                    options=[{'label':i,'value':i} for i in ["j'aime",'collection']],
                    multi=False,

                )
            ]
        )

    def layout_for_display_board(self):
        """
        It takes a list of dictionaries, and for each dictionary in the list, it creates a card with the
        class name, value, and unit specified in the dictionary
        :return: A list of html.Div objects.
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
                            }
                    ]
        layout = html.Div(
            id = 'page-board-display',
            className='page-board-display',
            children=[    self.htmlcreate.get_card_of_boardgame(i,play[0],play[1],self.conf.list_mesure) for i,play in enumerate(self.conf.list_demo_jeux)]
            
        )
        return layout


    def make_icon_see_filter(self):
        """
        It creates a div with three divs inside it.
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