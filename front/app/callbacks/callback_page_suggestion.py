from ast import In
from tkinter import ALL
from dash.dependencies import Input, Output,State,MATCH
from dash.dash import no_update
from resources.htmlCreate import HtmlCreate

def import_all_callback_page_suggetion(app):

    
    @app.callback(Output(component_id='button_mystery',component_property='className'),
                Output(component_id='part_display_mystery',component_property='className'),
                Output(component_id='button_mystery',component_property='n_clicks'),
           

                Input(component_id='button_mystery',component_property='n_clicks'),
                Input(component_id='button_mystery_new_tirage',component_property='n_clicks'),
                State(component_id='button_mystery',component_property='className'),
                State(component_id='part_display_mystery',component_property='className'),
                )
             
    def make_active_button_mystery(nclick,nclick_2,classname,classname_new):
        """
        If the first button is clicked, then the first button is made active and the second button is
        made inactive. If the second button is clicked, then the second button is made active and the
        first button is made inactive
        
        :param nclick: is the number of clicks on the button
        :param nclick_2: is the number of clicks on the button
        :param classname: the class of the button that is clicked
        :param classname_new: the class of the div that I want to change
        :return: a tuple of three values.
        """
        if nclick:

            classnew = 'button_mystery' if 'active' in classname else'button_mystery active'
            classnew_mystery = 'part_display_mystery active'
            return  classnew,classnew_mystery,0

        elif nclick_2:
      
            classnew_mystery = 'part_display_mystery active3' if 'active2' in classname_new else 'part_display_mystery active2'
  
            return no_update,classnew_mystery,0

        return no_update,no_update,no_update


    @app.callback(Output(component_id={'type':'card_mystery_cont','index':MATCH},component_property='className'),
                
                Input(component_id={'type':'card_mystery_cont','index':MATCH},component_property='n_clicks'),
              
                State(component_id={'type':'card_mystery_cont','index':MATCH},component_property='className'),
                
             )
    def make_active_for_card_mystery(nclick ,classname):
        """
        If the number of clicks is greater than 0, then return the string 'card_mystery_cont active',
        otherwise return the string 'no_update'
        
        :param nclick: the number of clicks
        :param classname: the classname of the div you want to update
        :return: a string.
        """
        if nclick:
            return 'card_mystery_cont active'
        return no_update

    @app.callback(      Output(component_id='part_left_mystery',component_property='children'),
                        Output(component_id='part_center_mystery',component_property='children'),
                        Output(component_id='part_right_mystery',component_property='children'),
                        Input(component_id='button_mystery_new_tirage',component_property='n_clicks'))

    def make_no_active_for_card_mystery(nclic_button):
        """
        If the button is clicked, then return the HTML for the three cards. Otherwise, return no_update
        for each card
        
        :param nclic_button: is a boolean that indicates if the button has been clicked or not
        :return: the output of the function
        HtmlCreate(app).get_layout_mystery_card(1),HtmlCreate(app).get_layout_mystery_card(2),HtmlCreate(app).get_layout_mystery_card(3)
        """
    
        if nclic_button:
            
            return HtmlCreate(app).get_layout_mystery_card(1),HtmlCreate(app).get_layout_mystery_card(2),HtmlCreate(app).get_layout_mystery_card(3)
        return no_update,no_update,no_update

