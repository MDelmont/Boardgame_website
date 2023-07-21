#!/usr/bin/env python
# -*- coding: utf-8 -*-

import dash
import logging
from datetime import datetime
import pytz
import requests
import flask
# The class App() is a class that contains the app.dash() and app.flask() objects.
class App():
    def __init__(self):
        """
        It initializes the app, and sets the launch time to the current time.
        """
  
        
        self.start_time = datetime.now()
        self.launch_time = pytz.timezone('Europe/Paris').localize(datetime.now()).strftime('%Y-%m-%d_%H_%M')

        logging.basicConfig(filename=f"./logs/outlogs_{self.launch_time}.log",level=logging.INFO)

        logging.info(f"[ INITIALISATION : APP for Back office {self.launch_time} ]")
        
    # meta_tags are required for the app layout to be mobile responsive
    dash.Dash()
    app_flask = flask.Flask(__name__)
    app = dash.Dash(__name__, server=app_flask, suppress_callback_exceptions=True,
                    meta_tags=[{'name': 'viewport','content': 'width=device-width, initial-scale=1.0'}] )
    server = app.server