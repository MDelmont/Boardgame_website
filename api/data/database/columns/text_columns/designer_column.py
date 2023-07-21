#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
from data.database.columns.column import Column
class Column_Designer(Column):
    def __init__(self):
        sql_name ='designer'
        name = 'designer'
        sql_type = 'TEXT'
  
        attribue=''
        presentation = []

        super().__init__(sql_name,name,sql_type,attribue,presentation)
