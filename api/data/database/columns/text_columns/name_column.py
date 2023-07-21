#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
from data.database.columns.column import Column
class Column_Name(Column):
    def __init__(self):
        sql_name ='name'
        name = 'Nom'
        sql_type = 'TEXT'
  
        attribue='NOT NULL UNIQUE'
        presentation = []

        super().__init__(sql_name,name,sql_type,attribue,presentation)
