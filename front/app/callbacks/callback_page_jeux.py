from dash.dependencies import Input, Output,State
from dash.dash import no_update
import logging
from pages.page_jeux import page_jeux
from pages.page_connection import Page_connection
from pages.page_home  import page_home
from pages.page_profil import Page_profil
from pages.page_suggestion import page_suggestion
def import_all_callback_page_jeux(app):
    @app.callback(Output(component_id='see_filter_jeux',component_property='className'),
                Input(component_id='see_filter_jeux',component_property='n_clicks'),
                State(component_id='see_filter_jeux',component_property='className'),
             )
    def make_active_see_filter_jeux(nclick ,classname):
        """
        If the number of clicks is greater than 0, then return the string 'see_filter' if the string
        'active' is in the classname, otherwise return the string 'see_filter active'. Otherwise, return
        the no_update function
        
        :param nclick: the number of clicks
        :param classname: the current classname of the element
        :return: a string.
        """
        if nclick:
            return 'see_filter' if 'active' in classname else 'see_filter active'
        return no_update