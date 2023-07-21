#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
from data.database.columns.column import Column
class Column_Id(Column):
    def __init__(self):
        sql_name ='id'
        name = 'id'
        sql_type = 'SERIAL'
        attribue='NOT NULL'
        presentation = []

        super().__init__(sql_name,name,sql_type,attribue,presentation)
