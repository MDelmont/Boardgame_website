#!/usr/bin/env python
# -*- coding: utf-8 -*-


import logging
from dash import html, dash_table
from sympy import EX
from simulateur.conf import Conf
from datetime import datetime
from dateutil.parser import parse
import psycopg2
class base_data():
    def __init__(self,app):
        self.app = app
        self.conf = Conf()
        self.DATABASE = self.conf.PROJECT_DATABASE_CREDENTIALS
    
    def add_values_in_table(self,table,values):
        '''
        'table' : Name of table in database
        'values' : list of dict [ {},{} ...]
            dict : need all dict have the same structure 
                key : name columns
                value : value
        '''

        logging.info(f'add_values_in_table in {table}')
        is_send = False
        try:
            
            cols = str((self.get_all_columns_in_list_value(values)))
            val= self.get_all_value_in_sql_format(values)
            
            sql_request = f""" 
                INSERT INTO  {table}{"("+cols+")"}
                VALUES  {val}
            """
            logging.info('sql_request')
            logging.info(sql_request)

            conn = self.get_conn_database()
            logging.info('0')
            cur = conn.cursor()
            logging.info('1')
            check = cur.execute(sql_request)
            logging.info('2')
            conn.commit()
            logging.info('3')

            cur.close()
            conn.close()
            logging.info(f'Sql request : {check}')
            is_send =  check == None
            return is_send
        except Exception as error:
            logging.error(f'in add_values_in_table : {error}')
            return is_send

    def get_all_columns_in_list_value(self,value):
        logging.info(f'starts get_all_columns_in_list_value for {value}')
        try:
            if isinstance(value,list):
                return ','.join(value[0].keys()) if value else ''
            elif isinstance(value,dict):
           
                return ','.join(value.keys()) if value else ''
        except Exception as error:
            logging.error(f" in get_all_columns_in_list_value : {error}")

    def get_all_value_in_sql_format(self,value):
        logging.info(f'starts get_all_value_in_sql_format for {value}')
        try:
            if isinstance(value,list):
           
                return str([[self.apply_formatage_type(val) for val in row.values()] for row in value]).replace('"',"").replace('[',"(").replace(']',")").replace("'NULL'","NULL")[1:-1]
            elif isinstance(value,dict):
            
                return str([self.apply_formatage_type(val) for val in value.values()]).replace('"',"").replace('[',"(").replace(']',")").replace("'NULL'","NULL")
        except Exception as error:
            logging.error(f" in get_all_columns_in_list_value : {error}")
    
    def apply_formatage_type(self,value):
        logging.info(f'apply_formatage_type for value : {value}')
        try:
            type_value = self.get_type_value(value)

            if type_value == 'TEXT':
                return self.format_text_to_sql(value)
            elif type_value == 'DATE':
                return self.format_date_to_sql(value)
            elif type_value == 'NUMBER':
                return self.format_number_to_sql(value)
            elif type_value == 'BOOLEAN':
                return self.format_boolean_to_sql(value)
            elif type_value == 'NONE':
                return self.format_none_to_sql(value)
        except Exception as error:
            logging.error(f"in apply_formatage_type : {error}")

    def get_type_value(self,value):
        logging.info(f'get_type_value for value : {value}')
        try:
            type_val= ''
            if self.check_if_date(value):
                type_val = 'DATE'
            elif self.check_if_number(value):
                type_val = 'NUMBER'
            elif self.check_if_bool(value):
                type_val = 'BOOLEAN'
            elif value in [None,'',[]]:
                type_val = 'NONE'
            elif isinstance(value,str):
                type_val =  'TEXT'
            
            else:
                type_val = 'UNKNWON'
            logging.info(f'type : {type_val}, value : {value}')
            return type_val
        except Exception as error:
            logging.error(f"in get_type_value : {error}")

    def check_if_bool(self,value):
        logging.info(f'check_if_bool for value : {value}')
        try:
         
            return True in [str(value).lower() in {'oui','non','x'},isinstance(value,bool)]
            
        except Exception as error:
            logging.error(f" in check_if_bool : {error}")

    def check_if_number(self,value):
        logging.info(f'check_if_number for value : {value}')
        try:
            return  True in [ isinstance(value, int), isinstance(value, float),self.is_str_int_or_float(value)] 
        except Exception as error:
            logging.error(f" in check_if_number : {error}")

    def is_str_int_or_float(self,value):
        logging.info(f'is_str_date for value : {value}')
        try: 
            int(value)
            return True

        except ValueError:
            try:
                float(value)
                return False
            except ValueError:
                return False

    def check_if_date(self,value):
        logging.info(f'check_if_date for value : {value}')
        try:
            return True in [self.is_str_date(value), isinstance(value, datetime),]
        except Exception as error:
            logging.error(f" in check_if_date : {error}")
            
    def is_str_date(self,value,fuzzy=False):
        logging.info(f'is_str_date for value : {value}')
        try: 
            parse(value, fuzzy=fuzzy)
            return True if '-' in value else False

        except ValueError:
            return False
        
    def format_text_to_sql(self,value):
        logging.info(f'format_text_to_sql for value : {value}')
        try:
            good_val = str(value).replace("'","")
            return f'{good_val}'
        except Exception as error:
            logging.error(f'format_text_to_sql : {error}')

    def format_date_to_sql(self,value):
        logging.info(f'format_date_to_sql for value : {value}')
        try:
            if isinstance(value,str):
                return parse(value).strftime('%Y-%m-%d')
            elif isinstance(value,datetime):
                return value.strftime('%Y-%m-%d')
        except Exception as error:

            logging.error(f" in format_date_to_sql : {error}")

    def format_number_to_sql(self,value):
        logging.info(f'format_number_to_sql for value : {value}')
        try:
            if isinstance(value,float) or ',' in str(value):
                return str(value).replace(",",".")
            else:
                return int(value)
        except Exception as error:
            logging.error(f" in format_number_to_sql : {error}")

    def format_boolean_to_sql(self,value):
        logging.info(f'format_boolean_to_sql for value : {value}')
        try:
            return "true" if str(value).lower() in {'oui', 'true'} else "false"
        except Exception as error:
            logging.error(f" in format_boolean_to_sql : {error}")

    def format_none_to_sql(self,value):
        logging.info(f'format_none_to_sql for value : {value}')
        return "NULL"
    def get_conn_database(self):
        logging.info('get_conn_database')
        try:
            conn = psycopg2.connect(host=self.DATABASE['host'], 
                                    database=self.DATABASE['database'], 
                                    user=self.DATABASE['user'], 
                                    password=self.DATABASE['password'],
                                    port=self.DATABASE['port'])
            return conn
        except Exception as error:
            logging.error(f'in get_conn_database : {error}')
        return None
    def close_cur_con(self,cur,conn):
        logging.info('close_cur_con')
        cur.close()
        conn.close()


