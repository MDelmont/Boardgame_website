#!/usr/bin/env python
# -*- coding: utf-8 -*-


from flask import Flask
from flask_restful import Resource, Api



#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
from datetime import datetime
import pytz
class App():
    def __init__(self):
  
        
        self.start_time = datetime.now()
        self.launch_time = pytz.timezone('Europe/Paris').localize(datetime.now()).strftime('%Y-%m-%d_%H_%M')

        logging.basicConfig(filename=f"logs\outlogs_{self.launch_time}.log",level=logging.INFO)

        logging.info(f"[ INITIALISATION : APP for Back office {self.launch_time} ]")
        
    # Start app_api
    app = Flask(__name__)
    api = Api(app)




