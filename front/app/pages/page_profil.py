#!/usr/bin/env python
# -*- coding: utf-8 -*-

import dash_bootstrap_components as dbc
from dash import html, dcc
from resources.htmlCreate import HtmlCreate

import logging
class Page_profil():
    def __init__(self,app):
        self.app = app
        self.titre = "Profil"
        self.htmlcreate = HtmlCreate(app)
        self.get_layout()
        
  
        
    def get_layout(self):
        """
        It returns a list of three elements, the first two of which are the results of two other
        functions, and the third of which is a string
        :return: The layout is being returned.
        """
        logging.info('Start make layout of Page_profil')
        layout=[]
        try:
            layout.append(self.get_layout_title(self.titre))
            layout.append(self.get_layout_formulaire_profil())
            layout.append(self.get_layout_for_modify_password())
        except Exception as error:
            logging.error(f'in get_layout  Page_profil : {error}')
        return layout


    def get_layout_title(self,name):
        """
        It takes a string as an argument and returns a div with the class name being the string with
        spaces replaced by underscores
        
        :param name: the name of the section
        :return: A Div with a className and children.
        """
        return html.Div(
            className='title_of_part_page_' + str(name).replace(' ','_'),
            children = name
        )

    def get_layout_formulaire_profil(self):
        """
        It returns a Div element with a className of 'formulaire_profil' and children of a bunch of
        other elements
        :return: The function get_layout_formulaire_profil() returns a Div element with the className
        'formulaire_profil'.
        """
        return html.Div(
            className='formulaire_profil',
            children=[
                self.get_layout_make_case('email'),
                html.Button(id='Modifier_le_mot_de_passe_profil',className='Modifier_le_mot_de_passe',children='Modifier le mot de passe'),
                html.Button(id='Effacer_ses_donnees_profil',className='Effacer_ses_donnees',children='Effacer ses données'),
                html.Button(id='Supprimer_le_compte_profil',className='Supprimer_le_compte',children='Supprimer le compte'),
                html.Button(id='Déconnexion_profil',className='Déconnexion',children='Déconnexion'),
                
                
            ]
        )

    def get_layout_for_modify_password(self):
        """
        It returns a div with a bunch of children
        :return: The return value is a Div element with the id form_modify_password_profil.
        """


        return html.Div(
            id='form_modify_password_profil',
            className='form_modify_password',
            children=[
         

                    self.get_layout_title('Modifier le mot de passe'),
                    self.get_layout_make_case('ancien mot de passe'),
                    self.get_layout_make_case('Nouveau mot de passe'),
                    self.get_layout_make_case('Noveau mot de passe'),
                    html.Button(className='Envoyer',children='Envoyer'),
                    html.Img(
                            id='close_img_password_profil',
                            className='close_img_password',
                            src= self.htmlcreate.get_img_encore_for_src(path='./front/app/assets/pages/profil/icon/cancel.png'),
                            alt='close'
                        ),
            ]
            

        )
    def get_layout_make_case(self,text):
        """
        It returns a div with two children, a div with a text and an input with a specific id and class
        
        :param text: the text that will be displayed in the form
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
                    id='input_of_make_case'+str(text).replace(' ','_'),
                    type="password" if  'mot de passe' in text  else 'email',
                    className='input_of_make_case'
                )
            ]
        )