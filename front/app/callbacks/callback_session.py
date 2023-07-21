from dash.dependencies import Input, Output,State
import uuid
from data.gestion_of_session import Gestion_of_session
import requests
import json
from dash.dependencies import Input, Output,State,MATCH, ALL
from dash.dash import no_update
def import_all_callback_session_id(app):

    
    @app.callback(Output(component_id='session-id',component_property='children'),

                Input(component_id='session-id',component_property='n_clicks'),
                State(component_id='session-id',component_property='n_clicks'))
             
    def make_sessin_id(session_click,session_id):

        if not session_id:
            do_request = True
            while do_request :
                session_id = uuid.uuid4()
                do_request =  requests.get(f'http://127.0.0.1:5000//consumer/session/{session_id}').json()['exist']
     
        return  str(session_id)


   

        