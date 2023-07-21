#!/usr/bin/env python
# -*- coding: utf-8 -*-
from data.database.tables.table import Tables
import logging

from data.database.columns.int_columns import id_mechanic,id_boardgame

class Table_boardgame_have_mechanic(Tables):
    def __init__(self,app):
    
        name = 'boardgame_have_mechanic'





        list_columns = [id_boardgame.Column_Id_boardgame(),
                        id_mechanic.Column_Id_mechanic()]
                        
                     

        list_primary_key = [id_boardgame.Column_Id_boardgame(),id_mechanic.Column_Id_mechanic()] 
        super().__init__(app,name,list_columns,list_primary_key=list_primary_key)
