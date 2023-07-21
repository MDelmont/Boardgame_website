#!/usr/bin/env python
# -*- coding: utf-8 -*-
from data.database.tables.table import Tables
import logging
from data.database.columns.text_columns import name_column
from data.database.columns.int_columns import id_column
class Table_mechanic(Tables):
    def __init__(self,app):
    
        name = 'mechanic'
        public_name='mécanique'
        list_columns = [id_column.Column_Id(),
                        name_column.Column_Name()]

                        
        list_primary_key = [id_column.Column_Id()] 
        super().__init__(app,name,list_columns,list_primary_key=list_primary_key,public_name=public_name)





    def add_value_in_table_with_id_and_unique(self,values):

        logging.info(f'add_value_in_table_with_id_and_unique in {self.name}')
        is_send=False
        try:
            cols = str((self.get_all_columns_in_list_value(values)))
            val= self.get_all_value_in_sql_format(values)

            sql_request = f'''    
                            INSERT INTO {self.name} ({cols}) values (
                            {val}) on conflict (name)
                            DO UPDATE SET 
                                name=EXCLUDED.name 
                            RETURNING id;

                '''
            logging.info('sql_request')
            logging.info(sql_request)
            print(sql_request)

            conn = self.get_conn_database()
  
            cur = conn.cursor()

            check = cur.execute(sql_request)
        
            id = cur.fetchone()[0]

            conn.commit()
            cur.close()
            conn.close()
            logging.info(f'Sql request : {check}')
            is_send =  check == None

            return is_send , id
       
        except Exception as error:
            logging.error(f'in add_value_in_table_with_id_and_unique : {error}')
            return is_send

