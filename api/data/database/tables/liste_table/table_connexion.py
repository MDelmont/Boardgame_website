#!/usr/bin/env python
# -*- coding: utf-8 -*-
from data.database.tables.table import Tables
import logging
from data.database.columns.text_columns import session_column
from data.database.columns.int_columns import id_consumer
class Table_connexion(Tables):
    def __init__(self,app):
    
        name = 'connexion'
        public_name='connexion'
        list_columns = [id_consumer.Column_Id_consumer(),
                        session_column.Column_session()]

                        
        list_primary_key = [id_consumer.Column_Id_consumer()] 
        super().__init__(app,name,list_columns,list_primary_key=list_primary_key,public_name=public_name)




    def get_session_exist_in_table(self,id_session):
        sql_request = f"""
            SELECT CASE WHEN EXISTS (
                Select * 
                from {self.name}
                where session ='{id_session}')
                THEN CAST(1 AS BIT)
                ELSE CAST(0 AS BIT) END
        """
        conn = self.get_conn_database()
        cur = conn.cursor()
        cur.execute(sql_request)
   
        resp = cur.fetchall()
 
        return True if resp[0][0] == '1'  else False

    def get_consumer_exist_in_table(self,id_consumer):
        sql_request = f"""
            SELECT CASE WHEN EXISTS (
                Select * 
                from {self.name}
                where id_consumer ='{id_consumer}')
                THEN CAST(1 AS BIT)
                ELSE CAST(0 AS BIT) END
        """
        conn = self.get_conn_database()
        cur = conn.cursor()
        cur.execute(sql_request)
   
        resp = cur.fetchall()
  
        return True if resp[0][0] == '1'  else False
    
    def get_id_with_session(self,id_session):
        sql_request = f"""
           
                Select id_consumer 
                from {self.name}
                where session ='{id_session}'
        """
        conn = self.get_conn_database()
        cur = conn.cursor()
        cur.execute(sql_request)
        resp = cur.fetchall()
        return resp[0][0]
    
    def add_update_session_in_connexion(self,id_consumer,session):

       
        if self.get_consumer_exist_in_table(id_consumer):
            return super().update_values_in_table(self.name,dict_value={'session':session},list_col=['session'],dict_where={ 'id_consumer' : ['AND','=',id_consumer,'TEXT']})
        else:
            return super().add_values_in_table({'session':session,
                                        'id_consumer':id_consumer})