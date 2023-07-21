#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
from data.database.columns.column import Column
class Column_Yearpublished(Column):
    def __init__(self):
        sql_name ='yearpublished'
        name = 'date de publication'
        sql_type = 'INT'
        attribue=''
        presentation = []

        super().__init__(sql_name,name,sql_type,attribue,presentation)