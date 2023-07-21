#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
from data.database.columns.column import Column
class Column_Wish(Column):
    def __init__(self):
        sql_name ='wish'
        name = 'Souhaite'
        sql_type = 'BOOL'

        attribue=''
        presentation = []

        super().__init__(sql_name,name,sql_type,attribue,presentation)
