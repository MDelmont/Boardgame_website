
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, request
from flask_restful import Resource, Api
from app.endpoints.boardgame import endpoint_boardgame
from app.endpoints.consumer import endpoint_consumer
from app.endpoints.mechanic import endpoint_mechanic
from app.endpoints.theme import endpoint_theme

from app.endpoints.endpoint_boardgame_mechanic import endpoint_boardgame_mechanic
from app.endpoints.endpoint_boardgame_theme import endpoint_boardgame_theme
from app.endpoints.endpoint_consumer_boardgame import endpoint_consumer_boardgame


def import_all_endpoint(app):
    endpoint_boardgame.import_endpoint_boardgame(app)
    endpoint_consumer.import_endpoint_consumer(app)
    endpoint_mechanic.import_endpoint_mechanic(app)
    endpoint_theme.import_endpoint_theme(app)
    endpoint_boardgame_mechanic.import_endpoint_boardgame_mechanic(app)
    endpoint_boardgame_theme.import_endpoint_boardgame_theme(app)
    endpoint_consumer_boardgame.import_endpoint_consumer_boardgame(app)
