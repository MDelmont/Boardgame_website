#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
from data.database.columns.column import Column
class Column_Email(Column):
    def __init__(self):
        sql_name ='Email'
        name = 'Email'
        sql_type = 'TEXT'

        attribue='NOT NULL'
        presentation = []

        super().__init__(sql_name,name,sql_type,attribue,presentation)
