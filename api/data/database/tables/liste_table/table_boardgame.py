#!/usr/bin/env python
# -*- coding: utf-8 -*-
from data.database.tables.table import Tables
import logging
from data.database.columns.text_columns import image_column,description_column,designer_column,name_column,little_description_column,source_url_column
from data.database.columns.int_columns import id_column,yearpublished,minplayers,maxplayers,minplaytime,maxplaytime,minage,maxage
from data.database.columns.float_columns import price
class Table_boardgame(Tables):
    def __init__(self,app):
    
        name = 'boardgame'
        public_name='Client'
        list_columns = [id_column.Column_Id(),
                        source_url_column.Column_Source_url(),
                        name_column.Column_Name(),
                        price.Column_price(),
                        yearpublished.Column_Yearpublished(),
                        image_column.Column_Image(),
                        description_column.Column_description(),
                        little_description_column.Column_little_description(),
                        minplayers.Column_Minplayers(),
                        maxplayers.Column_Maxplayers(),
                        minplaytime.Column_Minplaytime(),
                        maxplaytime.Column_Maxplaytime(),
                        minage.Column_Minage(),
                        maxage.Column_Maxage(),
                        designer_column.Column_Designer()]


        list_primary_key = [id_column.Column_Id()] 
        super().__init__(app,name,list_columns,list_primary_key=list_primary_key,public_name=public_name)




    def update_values_in_table(self, boardgame):


        list_col = boardgame.keys()
        dict_where = {
            'id':boardgame['id']
        }
        boardgame.pop('id')


        return super().update_values_in_table(self, list_col, dict_where, boardgame)
    
    def add_value_in_table_with_id_and_unique(self,values):

        logging.info(f'add_value_in_table_with_id_and_unique in {self.name}')
        is_send=False
        try:
            cols = str((self.get_all_columns_in_list_value(values)))
            val= self.get_all_value_in_sql_format(values)

            sql_request = f'''    
                            INSERT INTO {self.name} ({cols}) values 
                            {val} on conflict (name)
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



