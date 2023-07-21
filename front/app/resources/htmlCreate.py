#!/usr/bin/env python
# -*- coding: utf-8 -*-
from dash import html
from resources.conf import Conf
import base64
import random

class HtmlCreate():
    def __init__(self,app):
        self.conf = Conf()
        self.app = app
        
    def get_list_for_header(self,id ='',li_class_name='',name_of_part='Default',path_of_img=''):
        """
        It returns a list item with a link inside of it. 
        The link has a span with an image inside of it and a span with text inside of it.
        
        :param id: the id of the li element
        :param li_class_name: This is the name of the class that will be used to identify the li element
        :param name_of_part: The name of the part of the header you want to create, defaults to Default
        (optional)
        :param path_of_img: The path of the image you want to use
        :return: A list of html.Li() objects.
        """
        return html.Li(
            
            n_clicks=0,
            id=id,
            className=f"{id} {li_class_name}",
            children=[
                html.A(
                    #href=f'/{li_class_name}',
                    children=[
                        html.Span(
                            className='icon',
                            children=[
                                html.Img(
                                    className='img_icon',
                                    src=self.get_img_encore_for_src(path_of_img),
                                    #alt=name_of_part,
                                )
                            ]
                        ),
                        html.Span(
                            className='text',
                            
                            children=name_of_part,
                        ),
                    ]
                )
            ]
        )


    def get_pieces_html(self):
        """
        It returns a div with a div with a div with a div
        :return: A Div element with a className of 'cadre_pieces' and children of a Div element with a
        className of 'border_pieces' and children of a Div element with a className of 'border_pieces_2'
        and children of a Div element with a className of 'backgoud_pieces'
        """
        return html.Div(
            className='cadre_pieces',
            children=[
                html.Div(
                    className='border_pieces',
                    children=[
                        html.Div(
                            className='border_pieces_2',
                            children=[
                                html.Div(className='backgoud_pieces')
                            ]
                        )
                    ]
                )
            ]
        )

    def get_img_encore_for_src(self,path):
        """
        It takes a path to an image, opens it, encodes it, and returns the encoded image as a string
        
        :param path: The path to the image file
        :return: The image is being returned as a string.
        """
     
        encode_image = base64.b64encode(open(path,'rb').read())
        return 'data:image/png;base64,{}'.format(encode_image.decode())
  
    def get_card_for_header(self,color,name,path_img_color,path_img_white,path_img_black,number_card):
        """
        It returns a div with a bunch of nested divs and spans.
        
        :param color: the color of the card
        :param name: the name of the menu item
        :param path_img_color: the path to the colored image
        :param path_img_white: the path to the image that will be displayed on the front of the card
        :param path_img_black: the path to the black image
        :param number_card: the number of the card
        :return: A Div element with a bunch of children.
        """
        className=number_card
        if name == 'Accueil':
            className = f"{number_card} active"
        return html.Div(
            id=f'scene_{number_card}',
            className=f'scene_{className}',
            children=[
                 html.Div(className=f'poche poche_back'),
                 html.Div(className='Lines'),

                 html.Div(
                    className=f'card  {color}',
                    children=[
                        html.Div(
                            className='card__face card__face--front',
                            children=[
                                html.Span(className='text front',children=name),

                                html.Span(
                                className='icon',
                                children=[
                                    html.Img(
                                        className='img_icon front',
                                        src= self.get_img_encore_for_src(path_img_white),
                                        alt=name
                                    )
                                ])
                            ]
                        ),
                        
                        html.Div(
                            className='card__face card__face--back',
                            children=[
                                html.Div(
                                    className='line_border',
                                    children=[

                                        html.Span(className='number_card',children=number_card),

                                        html.Span(
                                        className='icon_border',
                                        children=[
                                            html.Img(
                                                className='img_icon border',
                                                src= self.get_img_encore_for_src(path_img_white),
                                                alt=name
                                            )
                                        ])
                                    ]
                                ),
                                html.Div(
                                    className='line_border_right',
                                    children=[

                                        html.Span(className='number_card',children=number_card),

                                        html.Span(
                                        className='icon_border',
                                        children=[
                                            html.Img(
                                                className='img_icon border',
                                                src= self.get_img_encore_for_src(path_img_color),
                                                alt=name
                                            )
                                        ])
                                    ]
                                ),
                                html.Span(className='text back',children=name),
                                html.Span(
                                className='icon_back',
                                children=[
                                    html.Img(
                                        className='img_icon back',
                                        src= self.get_img_encore_for_src(path_img_black),
                                        alt=name
                                    )
                                ]),
                                html.Div(
                                    className='point_num',
                                    children= self.get_card_point_menu(number_card)
                                )
                            ]),
                    ]),
                    html.Div(className='poche poche_front')
                ])
     
    def get_card_point_menu(self,number):
        """
        It takes a number as an argument and returns a list of 9 divs, each div is either a div with a
        class of 'point' or a div with a class of '' (empty string)
        
        :param number: the number of points to be displayed
        :return: A list of 9 Divs.
        """
        
        layout_vide = html.Div(className='')
        layout_point = html.Div(
                className='point',
                children=html.Div(className='middle_point')
        )

        dict_creation_des ={

            1:[ 0,0,0,
                0,1,0,
                0,0,0],
            2:[ 1,0,0,
                0,0,0,
                0,0,1,],
            3:[ 1,0,0,
                0,1,0,
                0,0,1,],
            4:[ 1,0,1,
                0,0,0,
                1,0,1,],
            5:[ 1,0,1,
                0,1,0,
                1,0,1,],
        }

        return [ layout_point if val else  layout_vide  for val in   dict_creation_des[number] ]

    def get_card_of_boardgame(self,number_of_board,title,img,list_of_mesure,forhome=False,forhomeheart=False,forhomecoll=False,forhomemore=False):
        """
        It returns a div with a title, an image, and a list of divs
        
        :param number_of_board: the number of the boardgame in the list of boardgames
        :param title: the title of the boardgame
        :param img: the image of the boardgame
        :param list_of_mesure: a list of dictionaries, each dictionary has a key and a value
        :param forhome: if the card is for the home page, defaults to False (optional)
        :param forhomeheart: if True, the heart icon will be displayed, defaults to False (optional)
        :param forhomecoll: if True, the card is displayed on the home page, and the collection icon is
        displayed, defaults to False (optional)
        :param forhomemore: if True, the more icon will be displayed, defaults to False (optional)
        :return: A Div element with a className of 'boardgame'
        """

        return html.Div(
            className='boardgame',
            children=[

                html.Div(
                    className='title_boardgame',
                    children=title
                ),

                html.Div(
                    className='img_board_cont',
                    children=html.Img(
                                    className='img_board',
                                    src=self.get_img_encore_for_src(img),
                            ),
                ),

                html.Div(
                    className='cont_info_board',
                    children=[self.make_info_card_of_boardgame(mesure) for mesure in list_of_mesure]

                ),
                html.Div(
                    className='icon_board_cont',
                    children=[self.make_icon_board_heart(number_of_board,forhomeheart,forhome),self.make_icon_board_more(number_of_board,forhomemore,forhome),self.make_icon_board_collection(number_of_board,forhomecoll,forhome)]

                ),


            ]
        )

    def make_info_card_of_boardgame(self,mesure):
        """
        It takes a dictionary as an argument and returns a div with two children divs. The first child
        div has a class name and a value, the second child div has a class name and a value.
        
        :param mesure: a dictionary with the following keys:
        :return: A Div element with two children Div elements.
        """
        return html.Div(

            className='info_board',
            children=[
                html.Div(

                    className=mesure['class'],
                    children=mesure['value']
                ),
                html.Div(

                    className='info_board_mesure',
                    children=mesure['unite']
                    
                ),
            
            ]
        )
    
    def make_icon_board_heart(self,number_of_board,forhomeheart,forhome,type='heart'):
        """
        It returns a div with a class of icon_board, which contains a div with an id of heart, and a
        class of heart
        
        :param number_of_board: the number of the board
        :param forhomeheart: if the heart is active or not
        :param forhome: if the heart is for the home page or not
        :param type: 'heart' or 'star', defaults to heart (optional)
        :return: A Div with a child Div.
        """
        return html.Div(
            className='icon_board',
            children=[
                html.Div(
                    id={'type': type if not forhome else 'hearthome','index':number_of_board},
                    className = 'heart'  if not forhomeheart else 'heart active')
            ]
        )
    
    def make_icon_board_more(self,number_of_board,forhomemore,forhome,type='more_icon'):
        """
        It creates a div with a class of icon_board, which contains a div with a class of more-icon,
        which contains two divs with a class of barre_one and barre_two
        
        :param number_of_board: the number of the board
        :param forhomemore: if the icon is for the home page or not
        :param forhome: if the icon is for the home page
        :param type: the type of icon, more_icon or less_icon, defaults to more_icon (optional)
        :return: A Div element with a className of icon_board.
        """
        return html.Div(
            className='icon_board',
            children=[
            
                html.Div(
                    id={'type':type if not forhome else 'more_icon_home','index':number_of_board},
                    className='more-icon' if not forhomemore else 'more-icon_home active',
                    children=[

                        html.Div(
                            className='barre_one'
                        ),
                        html.Div(
                            className='barre_two'
                        )


                    ]

                )
            ]
        )

    def make_icon_board_collection(self,number_of_board,forhomecoll,forhome,type='collection_icon'):
        """
        It returns a div with a class of icon_board, which contains a div with a class of collection,
        which contains a div with a class of box-cont, which contains a div with a class of box, which
        contains a div with a class of rack.
        
        :param number_of_board: the number of the board
        :param forhomecoll: if True, then the collection is for the home page
        :param forhome: if True, the collection is for the home page, if False, it's for the collection
        page
        :param type: this is the type of icon board, it can be collection_icon or collection_icon_home,
        defaults to collection_icon (optional)
        :return: A Div with a className of icon_board.
        """
        return html.Div(
            className='icon_board',
            children=[
         
                html.Div(
                    id = {'type':type if not forhome else 'collection_icon_home',
                            'index':number_of_board},
                    className = 'collection' if not forhomecoll else 'collection_home active',
                    
                    children=[
                        html.Div(
                            className = 'box-cont',
                            
                                children=[self.make_box_for_collection(color) for color in ['red','green','green2','yellow']]
                        ),
                        html.Div(
                            className = 'rack',
                            
                            
                        ),
                                
                    ]
                )


               
            ]
        )
    
    def make_box_for_collection(self,color):
        """
        It returns a Div element with a className of 'box' and a color, and three children Div elements
        with classNames of 'top-box', 'middle-box', and 'bottom-box'
        
        :param color: the color of the box
        :return: A Div element with a className attribute.
        """

        return html.Div(
            className=f'box {color}',
            children=[
                html.Div(
                    className=f'top-box',
                ),
                html.Div(
                    className=f'middle-box',
                ),
                html.Div(
                    className=f'bottom-box',
                )
            ]
        )
    
    def get_big_card_of_boardgame(self,number_of_board,title,img,list_of_mesure,desctiption_board,dict_attib_board,forhomeheart=False,forhomecoll=False):
        """
        It returns a list of html.Divs
        
        :param number_of_board: the number of the boardgame in the database
        :param title: the title of the game
        :param img: the image of the boardgame
        :param list_of_mesure: a list of dictionaries, each dictionary has the following keys:
        :param desctiption_board: a string
        :param dict_attib_board: a dictionary of the game's attributes
        :param forhomeheart: if the card is in the home page, it will be true, otherwise false, defaults
        to False (optional)
        :param forhomecoll: if the card is in the collection page, it will be true, defaults to False
        (optional)
        :return: A list of html.Div() objects.
        """


        return [

                html.Div(
                    className='img_board_cont',
                    children=html.Img(
                                    className='img_board',
                                    src=self.get_img_encore_for_src(img),
                            ),
                ),
                

                
                
                html.Div(
                    className='content_info',
                    children=[
                        html.Div(
                            className='title_boardgame_big',
                            children=title
                        ),

                        html.Div(
                            className='description_board',
                            children=desctiption_board
                        ),

                        html.Div(
                            className='univers_board',
                            children=[
                                self.get_layout_theme_meca_big(key,value) for key,value in dict_attib_board.items()

                            ]
                        ),

                        html.Div(
                            className='cont_info_board',
                            children=[self.make_info_card_of_boardgame(mesure) for mesure in list_of_mesure]

                        ),
                        html.Div(
                            className='icon_board_cont',
                            children=[self.make_icon_board_heart(number_of_board,forhomeheart,forhome=False,type='heart_big'),self.make_icon_star(number_of_board),self.make_icon_board_collection(number_of_board,forhomecoll,forhome=False,type='collection_icon_big')])

                ]),
                html.Div(
                    id='close_big_boardame',
                    className='close_img',
                    children=html.Img(
                                    className='img_board',
                                    src=self.get_img_encore_for_src('./front/app/assets/jeux/icon/cancel.png'),
                            ),
                ),
            ]
        

    def make_icon_star(self,number_of_board):
        """
        It creates a div with a class name of 'icon_board' and then creates a div with a class name of
        'stars_icon_cont' and then creates 5 divs with a class name of 'stars_icon' and then assigns an
        id to each of those 5 divs
        
        :param number_of_board: the number of the board
        :return: A Div with a className of icon_board.
        """
        return html.Div(
            className='icon_board',
            children=[
                html.Div(
                    id =f'stars_icon_cont_{number_of_board}',
                    className=f'stars_icon_cont',
                    children=[
                        html.Div(
                             id={'type':f'stars_icon_{i}','index':number_of_board},
                           
                            className='stars_icon',
                        )
                        for i in [5,4,3,2,1]
                    ]
                )
            ]
        )

    def get_layout_theme_meca_big(self,title,list_attrib):
        """
        It returns a div with a title and a list of divs with the same class name
        
        :param title: the title of the board
        :param list_attrib: a list of dictionaries, each dictionary has a key called 'name' and a key
        called 'value'
        :return: A Div element with a className of 'univ_board_cont' and children of a Div element with
        a className of 'title_univ' and children of title, and a Div element with a className of
        'list_univ' and children of a Div element with a className of 'univ_board' and children of
        attrib for each attrib in
        """
        return html.Div(
            className='univ_board_cont',
            children=[
                html.Div(
                    className='title_univ',
                    children=title

                ),
                html.Div(
                    className='list_univ',
                    children=[

                        html.Div(
                        className='univ_board',
                        children= attrib 

                ) for attrib in list_attrib
                    ]

                )
            ]
        )

    
    def get_layout_mystery_card(self,i):
        """
        It returns a div with two children, the first child is a div with two children, the first child
        of which is an img, and the second child of which is a div with two children, the first child of
        which is a div with two children, the first child of which is a div with two children, the first
        child of which is a div with two children, the first child of which is a div with two children,
        the first child of which is a div with two children, the first child of which is a div with two
        children, the first child of which is a div with two children, the first child of which is a div
        with two children, the first child of which is a div with two children, the first child of which
        is a div with two children, the first child of which is a div with two children, the first child
        of which is a div with two children, the first child of which is a div with two children
        
        :param i: the index of the card
        :return: A list of html.Div() objects.
        """
        list_mesure = self.conf.list_mesure
        y = random.randint(0,8)*i
        jeux= self.conf.list_demo_jeux[y]
        return html.Div(
            id={'type':'card_mystery_cont','index':i},
            className='card_mystery_cont',
            
            children=[
                html.Div(
                    className="card_mystery",
                    children=[ 

                         html.Img(
                                    className='img_board_cont_mystery',
                                    src=self.get_img_encore_for_src("./front/app/assets\pages\page_suggestion\mystery_jeux\image\interrogation.png"),
                                    #alt=name_of_part,
                                )
                    ]
                ),
                html.Div(
                    className="back_card_mystery",
                    children=self.get_card_of_boardgame(y,jeux[0],jeux[1],list_mesure)

                )
            ]
        )
    def get_layout_for_personne_not_connect(self):
        """
        It returns a Div element with a bunch of other elements inside it
        :return: A Div element with the id 'part_for_ask_connexion_cont' and the class
        'part_for_ask_connexion_cont'.
        """
        return html.Div(
            id='part_for_ask_connexion_cont',
            className='part_for_ask_connexion_cont',
            children=[

                html.Div(
                    className='part_for_ask_connexion',
                    children=[
                        html.Div('Merci de vous connecter pour utiliser cette fonctionnalité'),
                        html.Button(id='connexion_see',className='connection',children='se connecter'),
                        #html.Button(id='inscription_see',className='inscription',children="s'inscrire"),

                    ]
                ),
                html.Div(
                    id='close_ask_connection',
                    className='close_img',
                    children=html.Img(
                                    className='img_board',
                                    src=self.get_img_encore_for_src('./front/app/assets/jeux/icon/cancel.png'),
                            ),
                ),

            ]
        )