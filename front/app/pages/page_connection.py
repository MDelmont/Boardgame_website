#!/usr/bin/env python
# -*- coding: utf-8 -*-
import dash_bootstrap_components as dbc
from dash import html, dcc
from resources.htmlCreate import HtmlCreate
import logging
# It's a class that creates a layout for a page
class Page_connection():
    def __init__(self,app):
        """
        It's a constructor for the class Connection.
        
        :param app: the application object
        """
        self.app = app
        self.titre = "connection"
        self.get_layout()
    def get_layout(self):
        """
        Layout.append(self.get_layout_title())
        layout.append(self.get_layout_formulaire_connection())
        layout.append(self.get_layout_formulaire_inscription())
        :return: The layout of the page.
        """
        logging.info('Start make layout of Page_connection')
        layout=[]
        try:
            layout.append(self.get_layout_title())
            layout.append(self.get_layout_formulaire_connection())
            layout.append(self.get_layout_formulaire_inscription())
  

        except Exception as error:
            logging.error(f'in get_layout  Page_connection : {error}')

        return layout


    def get_layout_formulaire_inscription(self):
        """
        It returns a div with two children: a title and a form
        """
        logging.info('Start make layout of Page_inscription')

        try:
            return html.Div(
                className='Part_of_inscription',
                children=[
                
                    self.get_layout_title_inscription(),
                    self.get_layout_formulaire_inscription_detail()
                ]
            )
  

        except Exception as error:
            logging.error(f'in get_layout  formulaire_inscription : {error}')

   

    def get_layout_title_inscription(self):
        """
        It returns a div with a class name and a child
        :return: The title of the page
        """
        return html.Div(
            className='title_of_part_page_inscription',
            children = 'Inscription'
        )
    def get_layout_formulaire_inscription_detail(self):
        """
        It returns a Div containing a bunch of other Divs
        :return: a Div element with a className of 'formulaire_connection' and children of the result of
        the get_layout_make_case_inscription function.
        """
        return html.Div(
            className='formulaire_connection',
            children=[
                self.get_layout_make_case_inscription('email','email_page_inscri'),
                self.get_layout_make_case_inscription('mot de passe','mpd1_page_inscri'),
                self.get_layout_make_case_inscription('confirmer le mot de passe','mdp2_page_inscri'),
        
                html.Button(id='inscription_page_inscription',className='inscription',children="s'inscrire")
            ]
        )
        
    def get_layout_make_case_inscription(self,text,id):
        """
        It returns a div with two children, a div and an input. The div has a className and a child,
        which is a string. The input has an id, a type, and a className
        
        :param text: the text that will be displayed in the div
        :param id: the id of the input
        :return: A Div with a Div and an Input.
        """
        return html.Div(
            className='case_of_form',
            children=[
                html.Div(
                    className='text_of_case_of_form',
                    children=text
                ),
                dcc.Input(
                    id=id,
                    type="password" if text == 'mot de passe' else 'email',
                    className='input_of_make_case'
                )
            ]
        )
    def get_layout_title(self):
        """
        It returns a div with a className and a children attribute
        :return: a Div element with a className and children.
        """
        return html.Div(
            className='title_of_part_page_connection',
            children = 'Connexion'
        )
    def get_layout_formulaire_connection(self):
        """
        It returns a Div element with a className of 'formulaire_connection' and children of the return
        values of the get_layout_make_case function
        :return: The function get_layout_formulaire_connection is returning a Div element with the
        className 'formulaire_connection'.
        """
        return html.Div(
            className='formulaire_connection',
            children=[
                self.get_layout_make_case('email'),
                self.get_layout_make_case('mot de passe'),
                html.Button(id='connexion_page',className='connection',children='Connexion'),
              
            ]
        )
        
    def get_layout_make_case(self,text):
        """
        It returns a div with a div inside of it, and the inner div has a text inside of it
        
        :param text: the text that will be displayed in the case
        :return: A Div with a Div and an Input
        """
        return html.Div(
            className='case_of_form',
            children=[
                html.Div(
                    className='text_of_case_of_form',
                    children=text
                ),
                dcc.Input(
                    id=f'connexion_{str(text).replace(" ","_")}',
                    type="password" if text == 'mot de passe' else 'email',
                    className='input_of_make_case'
                )
            ]
        )