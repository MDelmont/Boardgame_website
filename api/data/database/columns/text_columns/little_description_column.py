#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
from data.database.columns.column import Column
class Column_little_description(Column):
    def __init__(self):
        sql_name ='little_description'
        name = 'Petit description'
        sql_type = 'TEXT'
  
        attribue=''
        presentation = []

        super().__init__(sql_name,name,sql_type,attribue,presentation)
