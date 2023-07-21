from ast import In
from dash.dependencies import Input, Output,State,MATCH, ALL
from dash.dash import no_update
import logging
import dash
from resources.htmlCreate import HtmlCreate
from resources.conf import Conf
import json

def import_all_callback_boardgame_card(app):
    
    @app.callback(Output(component_id={'type':'heart','index':MATCH},component_property='className'),
                Input(component_id={'type':'heart','index':MATCH},component_property='n_clicks'),
                State(component_id={'type':'heart','index':MATCH},component_property='className'),
             )
    def make_active_or_not_heart_boardgame(nclick ,classname):
        """
        If the user has clicked the heart, then return 'heart' if 'active' is in the classname,
        otherwise return 'heart active'. 
        If the user has not clicked the heart, then return no_update
        
        :param nclick: the number of clicks
        :param classname: the current classname of the element
        :return: a string.
        """
        if nclick:
            return 'heart' if 'active' in classname else 'heart active'
        return no_update

    @app.callback(
             
                Output(component_id={'type':'heart_big','index':MATCH},component_property='className'),
                Input(component_id={'type':'heart_big','index':MATCH},component_property='n_clicks'),
                State(component_id={'type':'heart_big','index':MATCH},component_property='className'),
             )
    def make_active_or_not_heart_big_boardgame(nclick ,classname):
        """
        If the number of clicks is greater than zero, return the string 'heart' if the string 'active'
        is in the classname, otherwise return the string 'heart active'
        
        :param nclick: the number of clicks
        :param classname: the current classname of the element
        :return: a string.
        """
        if nclick:
            return 'heart' if 'active' in classname else 'heart active'
        return no_update
    @app.callback(Output(component_id={'type':'collection_icon','index':MATCH},component_property='className'),
                Input(component_id={'type':'collection_icon','index':MATCH},component_property='n_clicks'),
                State(component_id={'type':'collection_icon','index':MATCH},component_property='className'),
             )
    def make_active_or_not_collection_boardgame(nclick,classname):
        """
        If the number of clicks is greater than zero, then return the string 'collection' if the string
        'active' is in the classname, otherwise return the string 'collection active'. Otherwise, return
        the value of the no_update variable
        
        :param nclick: the number of clicks
        :param classname: the classname of the element that was clicked
        :return: a string.
        """
        if nclick:
            return 'collection' if 'active' in classname else 'collection active'
        return no_update
    @app.callback(Output(component_id={'type':'collection_icon_big','index':MATCH},component_property='className'),
                Input(component_id={'type':'collection_icon_big','index':MATCH},component_property='n_clicks'),
                State(component_id={'type':'collection_icon_big','index':MATCH},component_property='className'),
             )
    def make_active_or_not_collection_boardgame_bug(nclick,classname):
        """
        If the number of clicks is greater than zero, then return the string 'collection' if the string
        'active' is in the classname, otherwise return the string 'collection active'. Otherwise, return
        the value of the no_update variable
        
        :param nclick: the number of clicks
        :param classname: the classname of the element that was clicked
        :return: a string.
        """
        if nclick:
            return 'collection' if 'active' in classname else 'collection active'
        return no_update



    @app.callback(Output(component_id={'type':'stars_icon_1','index':MATCH},component_property='className'),
                    Output(component_id={'type':'stars_icon_2','index':MATCH},component_property='className'),
                    Output(component_id={'type':'stars_icon_3','index':MATCH},component_property='className'),
                    Output(component_id={'type':'stars_icon_4','index':MATCH},component_property='className'),
                    Output(component_id={'type':'stars_icon_5','index':MATCH},component_property='className'),
                    Output(component_id={'type':'stars_icon_1','index':MATCH},component_property='n_clicks'),
                    Output(component_id={'type':'stars_icon_2','index':MATCH},component_property='n_clicks'),
                    Output(component_id={'type':'stars_icon_3','index':MATCH},component_property='n_clicks'),
                    Output(component_id={'type':'stars_icon_4','index':MATCH},component_property='n_clicks'),
                    Output(component_id={'type':'stars_icon_5','index':MATCH},component_property='n_clicks'),

                    Input(component_id={'type':'stars_icon_1','index':MATCH},component_property='n_clicks'),
                    Input(component_id={'type':'stars_icon_2','index':MATCH},component_property='n_clicks'),
                    Input(component_id={'type':'stars_icon_3','index':MATCH},component_property='n_clicks'),
                    Input(component_id={'type':'stars_icon_4','index':MATCH},component_property='n_clicks'),
                    Input(component_id={'type':'stars_icon_5','index':MATCH},component_property='n_clicks'),
             )
    def make_active_or_not_collection_boardgame(stars_icon_1_nclicks,stars_icon_2_nclicks,stars_icon_3_nclicks,stars_icon_4_nclicks,stars_icon_5_nclicks):
        """
        If the number of clicks on a star icon is greater than 0, then the star icon is active,
        otherwise it is not active
        
        :param stars_icon_1_nclicks: number of clicks on the first star
        :param stars_icon_2_nclicks: 0
        :param stars_icon_3_nclicks: 0
        :param stars_icon_4_nclicks: 0
        :param stars_icon_5_nclicks: 0
        :return: A tuple of strings.
        """
        list_star =['stars_icon active' if stars_icon else 'stars_icon'  for stars_icon in [stars_icon_1_nclicks,stars_icon_2_nclicks,stars_icon_3_nclicks,stars_icon_4_nclicks,stars_icon_5_nclicks]]
        
        list_star.extend([0,0,0,0,0])
        return tuple(list_star)

    @app.callback(
                Output(component_id='boardgame_big',component_property='className'),
                Output(component_id='boardgame_big',component_property='children'),
                Output(component_id='close_big_boardame',component_property='n_clicks'),
                Input(component_id={'type':'more_icon','index':ALL},component_property='n_clicks'),
                Input(component_id='close_big_boardame',component_property='n_clicks')
             )
    def make_active_big_boardgame(nclick,click_close_big_boardame):
        """
        If the user clicks on the close button, the big boardgame is closed. If the user clicks on a
        boardgame, the big boardgame is opened and the content is updated
        
        :param nclick: a list of booleans, one for each card. If the user clicks on a card, the
        corresponding boolean is set to True
        :param click_close_big_boardame: a boolean that is True when the user clicks on the close button
        of the big boardgame card
        :return: a tuple of three elements.
        """
        index_component = str(dash.callback_context.triggered[0]["prop_id"].split(".")[0].split(',')[0]).split(':')
   
        
        if click_close_big_boardame:
            return 'boardgame_big',no_update,0
        if True in [i != None for i in  nclick]:
            id = int(index_component[1])
  
            return 'boardgame_big active',HtmlCreate(app).get_big_card_of_boardgame(id,Conf().list_demo_jeux[id][0],Conf().list_demo_jeux[id][1],Conf().list_mesure,Conf().list_demo_jeux[id][2],Conf().dict_atrib),0
        return no_update,no_update,no_update



    
    
    
    





  
