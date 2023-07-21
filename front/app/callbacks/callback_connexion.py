#!/usr/bin/env python
# -*- coding: utf-8 -*-


from dash.dependencies import Input, Output,State,MATCH, ALL
import uuid
import requests
import json
from dash.dash import no_update
import json
def import_all_callback_connexion(app):


    @app.callback(

                Output('part_for_ask_connexion_cont','className'),
                Output('close_ask_connection','n_clicks'),
               

                
                
        
                Input(component_id='close_ask_connection',component_property='n_clicks'),
                Input(component_id='scene_2',component_property='className'),
                Input(component_id='scene_4',component_property='className'),
                Input(component_id='connexion_see',component_property='n_clicks'),
      

                 
                Input(component_id={'type':'heart','index':ALL},component_property='className'),
                Input(component_id={'type':'heart_big','index':ALL},component_property='className'),
                Input(component_id={'type':'collection_icon','index':ALL},component_property='className'),
                Input(component_id={'type':'collection_icon_big','index':ALL},component_property='className'),
                Input(component_id={'type':'stars_icon_1','index':ALL},component_property='className'),
                Input(component_id={'type':'stars_icon_2','index':ALL},component_property='className'),
                Input(component_id={'type':'stars_icon_3','index':ALL},component_property='className'),
                Input(component_id={'type':'stars_icon_4','index':ALL},component_property='className'),
                Input(component_id={'type':'stars_icon_5','index':ALL},component_property='className'),
                State(component_id='session-id',component_property='children'))
             
    def make_ask_connection(close_ask_connection,scene_2,scene_4,connexion_see,        
                            heard_list,big_heart,collection_list,big_coll,
                            stars_icon_1,stars_icon_2,stars_icon_3,stars_icon_4,stars_icon_5,session_id):
        """
        If the user is connected, the function returns a string with the class
        'part_for_ask_connexion_cont active' and a 0.
        
        If the user is not connected, the function returns a string with the class
        'part_for_ask_connexion_cont' and a 0.
        
        :param close_ask_connection: a boolean that is True when the user clicks on the "connect" button
        :param scene_2: a list of classes
        :param scene_4: a list of classes
        :param connexion_see: a boolean that is True when the user is connected
        :param heard_list: list of buttons
        :param big_heart: list of divs
        :param collection_list: list of all the collections
        :param big_coll: list of classNames
        :param stars_icon_1: list of stars_icon_1
        :param stars_icon_2: [div.stars_icon_2, div.stars_icon_2, div.stars_icon_2, div.stars_icon_2,
        div.stars_icon_2]
        :param stars_icon_3: [div.stars_icon_3, div.stars_icon_3.active]
        :param stars_icon_4: [div class="stars_icon_4 active"]
        :param stars_icon_5: list of 5 stars
        :param session_id: the session id of the user
        :return: a tuple.
        """

        list_check = [
            scene_2,scene_4,
                            *heard_list,*big_heart,*collection_list,*big_coll,
                            *stars_icon_1,*stars_icon_2,*stars_icon_3,*stars_icon_4,*stars_icon_5
                                ]
    
        try:
            is_connect =  True#json.loads(requests.get(f'http://127.0.0.1:5000//consumer/session/{session_id}').text)['exist']
  
        except Exception as error:
            is_connect = False
        if close_ask_connection or connexion_see:
            return 'part_for_ask_connexion_cont',0
        elif not is_connect:
            for className in list_check:
                if 'active' in className:
                    return 'part_for_ask_connexion_cont active',0
            else:
                return 'part_for_ask_connexion_cont',0
        else:
            return 'part_for_ask_connexion_cont',0

    @app.callback(

                
                Output(component_id='connexion_page',component_property='n_clicks'),
                Input(component_id='connexion_page',component_property='n_clicks'),
                State(component_id='connexion_email',component_property='value'),
                State(component_id='connexion_mot_de_passe',component_property='value'),
                State(component_id='session-id',component_property='children'))
    def make_connexion_for_app(connexion_page,connexion_email,connexion_mot_de_passe,session_id):
        if connexion_page:
            json_file = {'email':connexion_email,
                        'password':connexion_mot_de_passe,
                        'session_id':session_id
            }
         
        

            is_connect =  json.loads(requests.post(f'http://127.0.0.1:5000//consumer/connection',json=json_file).text)
    
            print(is_connect)
            return 0
                