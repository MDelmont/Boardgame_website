#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
from data.database.columns.column import Column
class Column_Id_theme(Column):
    def __init__(self):
        sql_name ='id_theme'
        name = 'id_theme'
        sql_type = 'INT'
        attribue='NOT NULL REFERENCES theme ON DELETE RESTRICT'
        presentation = []

        super().__init__(sql_name,name,sql_type,attribue,presentation)