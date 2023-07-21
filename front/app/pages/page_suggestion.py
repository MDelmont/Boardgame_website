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

class page_suggestion():
    def __init__(self,app):
        self.app = app
        self.htmlcreate = HtmlCreate(app)

    def get_layout(self):
        """
        It returns a list of two elements, the first element is a list of two elements, the second
        element is a list of two elements
        :return: A list of two elements.
        """
        logging.info('Start make layout of page_suggestion')
        layout=[]
        try:
            
            layout.append(self.get_layout_selection_part())
            layout.append(self.get_layout_display_cart_mystery())
        except Exception as error:
            logging.error(f'in get_layout  page_suggestion : {error}',exc_info=True)
        return layout

    def get_layout_display_cart_mystery(self):
        """
        It returns a div with three divs inside, each of which contains a card.
        :return: The return value is a Div element.
        """

        return html.Div(
            id='part_display_mystery',
            className='part_display_mystery',
            children=[

                html.Div(
                    className='part_new_tirage_mystery',
                    children=[
                         html.Div(
                            id='button_mystery_new_tirage',
                            className='button_mystery',
                            children=[
                                html.Span(
                                    className='text',
                                    children='Nouveau tirage !'
                                )
                            ]
                        )
                    ]
                ),
                html.Div(
                    id='part_left_mystery',
                    className='part_left_mystery',
                    children=[
                         self.htmlcreate.get_layout_mystery_card(1)
                    ]
                ),
                html.Div(
                    id='part_center_mystery',
                    className='part_center_mystery',
                    children=[
                         self.htmlcreate.get_layout_mystery_card(2)
                    ]
                ),
                html.Div(
                    id='part_right_mystery',
                    className='part_right_mystery',
                    children=[
                         self.htmlcreate.get_layout_mystery_card(3)
                    ]
                ),

                
            ]
        )
    def get_layout_selection_part(self):
        """
        It returns a Div element with a className of 'part_of_suggestion' and a child Div element with a
        className of 'button_mystery_cont' and a child Div element with an id of 'button_mystery' and a
        className of 'button_mystery' and a child Span element with a className of 'text' and a child
        string of 'Clic ici pour dénicher tes meilleures jeux de société'
        :return: A Div element with a className of 'part_of_suggestion'
        """
        return html.Div(
            className='part_of_suggestion',
            children=[
                html.Div(
                    className='button_mystery_cont',
                    children=[
                        html.Div(
                            id='button_mystery',
                            className='button_mystery',
                            children=[
                                html.Span(
                                    className='text',
                                    children='Clic ici pour dénicher tes meilleures jeux de société'
                                )
                            ]
                        )
                    ]
                )
            ]
        )


