from dash.dependencies import Input, Output,State
from dash.dash import no_update
import dash
import logging

def import_all_callback_page_profil(app):


    @app.callback(Output(component_id='form_modify_password_profil',component_property='className'),
                Output(component_id='Modifier_le_mot_de_passe_profil',component_property='n_clicks'),
                Output(component_id='close_img_password_profil',component_property='n_clicks'),
                Input(component_id='Modifier_le_mot_de_passe_profil',component_property='n_clicks'),
                Input(component_id='close_img_password_profil',component_property='n_clicks'),
                State(component_id='form_modify_password_profil',component_property='className'),
             )
    def make_active_see_filter_profil(modif_click,close_click ,classname):
        """
        If the user clicks on the "modif_click" button, then the classname of the div will be changed to
        "form_modify_password active" and the div will be displayed.
        
        If the user clicks on the "close_click" button, then the classname of the div will be changed to
        "form_modify_password" and the div will be hidden.
        
        If the user clicks on the "modif_click" button and the classname of the div is already
        "form_modify_password active", then the classname of the div will be changed to
        "form_modify_password" and the div will be hidden.
        
        If the user clicks on the "close_click" button and the classname of the div is already
        "form_modify_password", then the classname of the div will be changed to "form_modify_
        
        :param modif_click: the id of the button that opens the modal
        :param close_click: the id of the button that closes the modal
        :param classname: the classname of the element that was clicked
        :return: a tuple of three elements.
        """
        ctx = dash.callback_context

        if modif_click or close_click:
            return ('form_modify_password',0,0) if 'active' in classname else ('form_modify_password active',0,0)
        return no_update,no_update,no_update



    