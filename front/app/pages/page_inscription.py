#!/usr/bin/env python
# -*- coding: utf-8 -*-
import dash_bootstrap_components as dbc
from dash import html, dcc
from resources.htmlCreate import HtmlCreate
import logging
class Page_inscription():
    def __init__(self,app):
        """
        It creates a new instance of the class Inscription, and assigns the value of the parameter app
        to the attribute app of the instance.
        
        :param app: the app that is running the window
        """
        self.app = app
        self.titre = "inscription"
        self.get_layout()
    def get_layout(self):
        """
        Layout.append(self.get_layout_title_inscripition())
        layout.append(self.get_layout_formulaire_inscription())
        :return: The layout of the page.
        """
        logging.info('Start make layout of Page_inscription')
        layout=[]
        try:
            layout.append(self.get_layout_title_inscripition())
            layout.append(self.get_layout_formulaire_inscription())
  

        except Exception as error:
            logging.error(f'in get_layout  Page_inscription : {error}')

        return layout

    def get_layout_title_inscripition(self):
        """
        It returns a div with a class name and a child
        :return: a Div element with a className and children.
        """
        return html.Div(
            className='title_of_part_page_inscription',
            children = 'Inscription'
        )
    def get_layout_formulaire_inscription(self):
        """
        It returns a div with a class name of 'formulaire_connection' and children of the return values
        of the get_layout_make_case function
        :return: a Div element with a className of 'formulaire_connection' and children of the result of
        the get_layout_make_case function.
        """
        return html.Div(
            className='formulaire_connection',
            children=[
                self.get_layout_make_case('email','email_page_inscri'),
                self.get_layout_make_case('mot de passe','mpd1_page_inscri'),
                self.get_layout_make_case('confirmer le mot de passe','mdp2_page_inscri'),
        
                html.Button(id='inscription_page_inscription',className='inscription',children="s'inscrire")
            ]
        )
        
    def get_layout_make_case(self,text,id):
        """
        It returns a div with two children, a div and an input. The div has a class name and a child,
        which is a string. The input has an id, a type, and a class name
        
        :param text: the text that will be displayed in the div
        :param id: the id of the input
        :return: A Div element with a className of case_of_form.
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