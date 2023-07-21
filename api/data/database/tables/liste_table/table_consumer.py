#!/usr/bin/env python
# -*- coding: utf-8 -*-
from data.database.tables.table import Tables
import logging
from data.database.columns.text_columns import email_column,password_column
from data.database.columns.int_columns import id_column
import bcrypt
class Table_consumer(Tables):
    def __init__(self,app):
    
        name = 'consumer'
        public_name='Client'
        list_columns = [id_column.Column_Id(),email_column.Column_Email(),password_column.Column_Password()]
        list_primary_key = [id_column.Column_Id()] 
        super().__init__(app,name,list_columns,list_primary_key=list_primary_key,public_name=public_name)

    def add_consumer_in_table(self,email,password):

        email = str(email)
        password = str(password).encode('utf8')
        hash_password = bcrypt.hashpw(password, bcrypt.gensalt())

        value = {'email':email,'password':hash_password}
        return super().add_values_in_table(value,returning_id=True)

    def get_id_consumer_in_table(self,email):

        email = str(email)
        dict_condition = { 'email' : ['AND','=',email,'TEXT']}
      
        id=  super().select_value_in_table(['id'],dict_condition)
        if id :
            return id[0]['id']
   
        return None

    def update_values_in_table(self, consumers):

        list_col = consumers.keys()
        dict_where = {
            'id':consumers['id']
        }
        consumers.pop('id')
        return super().update_values_in_table(self, list_col, dict_where, consumers)
    
    def check_if_password_is_good(self,email,password):

        sql_request = f"""
                Select password 
                from consumer
                where (email ='{str(email).encode('utf8')}')
            
        """
        print(sql_request)
        conn = self.get_conn_database()
        cur = conn.cursor()
        cur.execute(sql_request)
   
        resp = cur.fetchall()
        print(resp)
        password_inbase =resp[0][0]
  
        return bcrypt.checkpw(str(password).encode('utf8'), str(password_inbase).encode('utf8'))



    

    



