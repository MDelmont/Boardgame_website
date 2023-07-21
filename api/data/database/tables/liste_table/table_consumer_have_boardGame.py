#!/usr/bin/env python
# -*- coding: utf-8 -*-
from data.database.tables.table import Tables
import logging
from data.database.columns.text_columns import name_column
from data.database.columns.int_columns import id_consumer,id_boardgame,score
from data.database.columns.bool_columns import have_column,wish_column
class Table_consumer_have_boardgame(Tables):
    def __init__(self,app):
    
        name = 'consumer_and_boardgame'





        list_columns = [id_consumer.Column_Id_consumer(),
                        id_boardgame.Column_Id_boardgame(),
                        score.Column_Score(),
                        have_column.Column_Have(),
                        wish_column.Column_Wish()
                        ]

        list_primary_key = [id_consumer.Column_Id_consumer(),id_boardgame.Column_Id_boardgame(),] 
        super().__init__(app,name,list_columns,list_primary_key=list_primary_key)
