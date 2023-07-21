from calendar import c
from dash.dependencies import Input, Output,State
from dash.dash import no_update
import logging
from pages.page_jeux import page_jeux
from pages.page_connection import Page_connection
from pages.page_home  import page_home
from pages.page_profil import Page_profil
from pages.page_suggestion import page_suggestion
from pages.page_list import page_list
from pages.page_inscription import Page_inscription
import requests
import dash
def import_all_callback_barre_menu(app):

    get_layout_page = {

            'accueil': page_home(app).get_layout(),
            'profil': Page_profil(app).get_layout(),
            'connection': Page_connection(app).get_layout(),
            'jeux': page_jeux(app).get_layout(),
            'suggestion': page_suggestion(app).get_layout(),
            'list':page_list(app).get_layout(),
            'inscription': Page_inscription(app).get_layout()
        }

    
    @app.callback(
                Output('page-content', 'children'),
                

           
                
                
                Input(component_id='list-1',component_property='className'),
                Input(component_id='list-2',component_property='className'),
                Input(component_id='list-3',component_property='className'),
                Input(component_id='list-4',component_property='className'),
                Input(component_id='list-5',component_property='className'),
                Input(component_id='scene_1',component_property='className'),
                Input(component_id='scene_2',component_property='className'),
                Input(component_id='scene_3',component_property='className'),
                Input(component_id='scene_4',component_property='className'),
                Input(component_id='scene_5',component_property='className'),
                Input(component_id='connexion_see',component_property='n_clicks'),
   
                State(component_id='session-id',component_property='children'))
    def update_url_of_page(list_1,list_2,list_3,list_4,list_5,scene_1,scene_2,scene_3,scene_4,scene_5,connexion_see,session_id):
        """
        If the user is connected, return the profile page, otherwise return the connection page
        
        :param list_1: the list of the first button
        :param list_2: the list of the id of the buttons in the list page
        :param list_3: the list of the id of the buttons in the navbar
        :param list_4: the list of the id of the button that was clicked
        :param list_5: the id of the button that was clicked
        :param scene_1: the id of the first tab
        :param scene_2: the id of the button that is clicked
        :param scene_3: the id of the button that is clicked
        :param scene_4: the id of the button that triggers the callback
        :param scene_5: the id of the button that triggers the callback
        :param connexion_see: a boolean that indicates whether the user has clicked on the "profile"
        button
        :param session_id: the session id of the user
        :return: the value of the variable get_layout_page['accueil']
        """

        is_connect = True# requests.get(f'http://127.0.0.1:5000//consumer/session/{session_id}').json()['exist']
        changed_id = [p['prop_id'] for p in dash.callback_context.triggered][0]

        if 'active' in scene_1 or 'active' in list_1:
            return get_layout_page['accueil']
        elif 'active' in scene_2 or 'active' in list_2:
            return  get_layout_page['list']
        elif 'active' in scene_3 or 'active' in list_3:
            return  get_layout_page['jeux']
        elif 'active' in scene_4 or 'active' in list_4:
            return  get_layout_page['suggestion']
        elif 'active' in scene_5 or 'active' in list_5 or connexion_see :
          
            return  get_layout_page['profil'] if is_connect else get_layout_page['connection']
            

        return get_layout_page['accueil']


    @app.callback(Output(component_id='list-1',component_property='n_clicks'),
                Output(component_id='list-2',component_property='n_clicks'),
                Output(component_id='list-3',component_property='n_clicks'),
                Output(component_id='list-4',component_property='n_clicks'),
                Output(component_id='list-5',component_property='n_clicks'),
                Output(component_id='list-1',component_property='className'),
                Output(component_id='list-2',component_property='className'),
                Output(component_id='list-3',component_property='className'),
                Output(component_id='list-4',component_property='className'),
                Output(component_id='list-5',component_property='className'),
                Output(component_id='scene_1',component_property='n_clicks'),
                Output(component_id='scene_2',component_property='n_clicks'),
                Output(component_id='scene_3',component_property='n_clicks'),
                Output(component_id='scene_4',component_property='n_clicks'),
                Output(component_id='scene_5',component_property='n_clicks'),
                Output('connexion_see','n_clicks'),
           

                Output(component_id='scene_1',component_property='className'),
                Output(component_id='scene_2',component_property='className'),
                Output(component_id='scene_3',component_property='className'),
                Output(component_id='scene_4',component_property='className'),
                Output(component_id='scene_5',component_property='className'),

                Input(component_id='list-1',component_property='n_clicks'),
                Input(component_id='list-2',component_property='n_clicks'),
                Input(component_id='list-3',component_property='n_clicks'),
                Input(component_id='list-4',component_property='n_clicks'),
                Input(component_id='list-5',component_property='n_clicks'),
                Input(component_id='scene_1',component_property='n_clicks'),
                Input(component_id='scene_2',component_property='n_clicks'),
                Input(component_id='scene_3',component_property='n_clicks'),
                Input(component_id='scene_4',component_property='n_clicks'),
                Input(component_id='scene_5',component_property='n_clicks'),
                Input(component_id='connexion_see',component_property='n_clicks'))
    def change_activate_class_of_item(list_1,list_2,list_3,list_4,list_5,scene_1,scene_2,scene_3,scene_4,scene_5,connexion_see):
        """
        If list_1 or scene_1 is True, then return 0,0,0,0,0, 'list-1
        active','list-2','list-3','list-4','list-5',0,0,0,0,0,0, 'scene_1
        active','scene_2','scene_3','scene_4','scene_5'
        
        If list_2 or scene_2 is True, then return 0,0,0,0,0, 'list-1','list-2
        active','list-3','list-4','list-5',0,0,0,0,0,0, 'scene_1','scene_2
        active','scene_3','scene_4','scene_5'
        
        If list_3 or scene_3 is True, then return 0,0,0,0,0, 'list-1','list
        
        :param list_1: is a boolean value that is True when the user clicks on the first item in the
        list
        :param list_2: is a boolean that is True when the user clicks on the second item in the list
        :param list_3: is a boolean that is True when the user clicks on the third item in the list
        :param list_4: is a boolean that is True when the user clicks on the 4th item in the list
        :param list_5: is a boolean that is true when the user clicks on the button "connexion"
        :param scene_1: the first scene
        :param scene_2: the name of the scene
        :param scene_3: is the name of the scene
        :param scene_4: is a boolean that is True when the user clicks on the button "scene_4"
        :param scene_5: is the connexion page
        :param connexion_see: boolean
        :return: a tuple of 20 elements.
        """
        
        if list_1 or scene_1:

            return 0,0,0,0,0, 'list-1 active','list-2','list-3','list-4','list-5',0,0,0,0,0,0, 'scene_1 active','scene_2','scene_3','scene_4','scene_5'
        elif list_2 or scene_2:

            return 0,0,0,0,0, 'list-1','list-2 active','list-3','list-4','list-5',0,0,0,0,0,0, 'scene_1','scene_2 active','scene_3','scene_4','scene_5'
        elif list_3 or scene_3:

            return 0,0,0,0,0, 'list-1','list-2','list-3  active','list-4','list-5',0,0,0,0,0,0, 'scene_1','scene_2','scene_3 active','scene_4','scene_5'
        elif list_4 or scene_4:

            return 0,0,0,0,0, 'list-1','list-2','list-3','list-4  active','list-5', 0,0,0,0,0,0,'scene_1','scene_2','scene_3','scene_4 active','scene_5'
        elif list_5 or scene_5 or connexion_see :
            return 0,0,0,0,0, 'list-1','list-2','list-3','list-4','list-5  active', 0,0,0,0,0,0, 'scene_1','scene_2','scene_3','scene_4','scene_5 active'



        return 0,0,0,0,0, no_update,no_update,no_update,no_update,no_update, 0,0,0,0,0,0, no_update,no_update,no_update,no_update,no_update









  
    