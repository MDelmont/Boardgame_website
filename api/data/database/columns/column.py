#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
class Column():
   
    def __init__(self,sql_name,name,sql_type,attribue,presentation=[]):
        self.sql_name = sql_name
        self.name = name
  
        self.sql_type = sql_type
 
        self.attribue=attribue
        self.presentation = presentation
        self.columns_dash =  {'name' : str(self.name),'id': str(self.sql_name) , 'presentation': str(self.presentation), 'type': 'text'} if self.presentation else {'name' : str(self.name),'id': str(self.sql_name), 'type': 'text'}

    def get_sql_create_name(self):
        return f"{self.sql_name} {self.sql_type} {self.attribue}"
    
    def get_dash_create_name(self):
        return {'name' : str(self.name),'id': str(self.sql_name) , 'presentation': str(self.presentation), 'type': 'text'} if self.presentation else {'name' : str(self.name),'id': str(self.sql_name), 'type': 'text'}

    