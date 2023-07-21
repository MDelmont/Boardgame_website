#!/usr/bin/env python
# -*- coding: utf-8 -*-
from data.database.tables.table import Tables
from data.database.columns.int_columns import id_theme,id_boardgame

class Table_boardgame_have_theme(Tables):
    def __init__(self,app):
    
        name = 'boardgame_have_theme'





        list_columns = [id_boardgame.Column_Id_boardgame(),
                        id_theme.Column_Id_theme()]
                        
                     

        list_primary_key = [id_boardgame.Column_Id_boardgame(), id_theme.Column_Id_theme()] 
        super().__init__(app,name,list_columns,list_primary_key=list_primary_key)
