#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
from data.database.columns.column import Column
class Column_bool(Column):
    def __init__(self):
        sql_name ='bool'
        name = 'bool'
        sql_type = 'TEXT'

        attribue='NOT NULL'
        presentation = []

        super().__init__(sql_name,name,sql_type,attribue,presentation)
