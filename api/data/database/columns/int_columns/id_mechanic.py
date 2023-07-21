#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
from data.database.columns.column import Column
class Column_Id_mechanic(Column):
    def __init__(self):
        sql_name ='id_mechanic'
        name = 'id_mécanique'
        sql_type = 'INT'
        attribue='NOT NULL REFERENCES mechanic ON DELETE RESTRICT'
        presentation = []

        super().__init__(sql_name,name,sql_type,attribue,presentation)