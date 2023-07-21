#!/usr/bin/env python
# -*- coding: utf-8 -*-

from data.database.resources.conf import Conf
import logging
import psycopg2
from datetime import datetime
from dateutil.parser import parse


class Tables():
    def __init__(self,app,name,list_columns,list_primary_key=[],public_name=''):
        self.app = app
        self.conf = Conf()
        self.DATABASE = self.conf.PROJECT_DATABASE_CREDENTIALS
        self.list_primary_key = list_primary_key
        self.name = name
        self.public_name=public_name
        self.list_columns = list_columns

    
    def creat_table_if_not_exist(self):
        '''
        Create table in database if not exist
        use self.name,self.DATABASE,self.List_columns
        '''
        logging.info(f'creat_table_if_not_exist in {self.name}')
    
        try:
       
            sql_request = f'''
                CREATE TABLE IF NOT EXISTS {self.name}
                ({','.join([ *[col.get_sql_create_name() for col in self.list_columns],
                            f"PRIMARY KEY ({','.join([col.sql_name for col in self.list_primary_key])})"])})
            '''
            logging.info('sql_request')
            logging.info(sql_request)
            print(sql_request )
            conn = self.get_conn_database()
     
    
          
            cur = conn.cursor()
        
            check = cur.execute(sql_request)
            cur.close()
                
            conn.commit()
            conn.close()
        except Exception as error:
            logging.error(f'in creat_table_if_not_exist : {error}')


    def select_value_in_table(self,col_need,dict_column_filtre={}):
    
        sql_request =   f"""  
                            Select {','.join(col_need)}
                            from {self.name}
                            {self.make_condition_columns(dict_column_filtre)}
                       """

                       
        logging.info('sql_request')
        logging.info(sql_request)

        conn = self.get_conn_database()

        cur = conn.cursor()
        cur.execute(sql_request)
        col  = [desc[0] for desc in cur.description]
        resp = cur.fetchall()
 


        cur.close()
        conn.close()

        return [ dict(zip(col,list(row))) for row in resp  ] if resp else []


    def add_values_in_table(self,values,returning_id=False):
        '''
        'values' : list of dict [ {},{} ...]
            dict : need all dict have the same structure 
                key : name columns
                value : value
        '''

        logging.info(f'add_values_in_table in {self.name}')
        is_send = False
        try:
            
            cols = str((self.get_all_columns_in_list_value(values)))
            val= self.get_all_value_in_sql_format(values)
            
            sql_request = f""" 
                INSERT INTO  {self.name}{"("+cols+")"}
                VALUES  {val}
                RETURNING id
            """ if returning_id else f""" 
                INSERT INTO  {self.name}{"("+cols+")"}
                VALUES  {val}
        
            """
            
            logging.info('sql_request')
            logging.info(sql_request)
            print(sql_request)

            conn = self.get_conn_database()
  
            cur = conn.cursor()

            check = cur.execute(sql_request)
        
            if returning_id:
                id = cur.fetchone()[0]

            conn.commit()
   

            cur.close()
            conn.close()
            logging.info(f'Sql request : {check}')
            is_send =  check == None
            if returning_id:
                return is_send , id
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
          
            if value in [None,'',[]]:
                type_val = 'NONE'
            elif self.check_if_number(value):
                type_val = 'NUMBER'
            elif self.check_if_date(value):
                type_val = 'DATE'
            elif self.check_if_bool(value):
                type_val = 'BOOLEAN'
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
            if value:
                return True in [self.is_str_date(value), isinstance(value, datetime)]
            return False
        except Exception as error:
            logging.error(f" in check_if_date : {error}")
            
    def is_str_date(self,value,fuzzy=False):
        logging.info(f'is_str_date for value : {value}')
        try: 
            if value:
                parse(value, fuzzy=fuzzy)
                return True if '-' in value else False
            return False
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


    def del_values_in_table(self,dict_column_filtre):
        sql_request =   f"""
                            Delete from {self.name}
                            {self.make_condition_columns(dict_column_filtre)}
                        """
        logging.info('sql_request')
        logging.info(sql_request)

        conn = self.get_conn_database()

        cur = conn.cursor()
        check = cur.execute(sql_request)
        conn.commit()

        cur.close()
        conn.close()
        logging.info(f'Sql request : {check}')

    def update_values_in_table(self,table,list_col,dict_where,dict_value):

        sql_request = f""" 
                UPDATE {table}
                SET {self.make_set_for_update(list_col,dict_value)}
                {self.make_condition_columns(dict_where)}
            """
        logging.info('sql_request')
        logging.info(sql_request)

        conn = self.get_conn_database()

        cur = conn.cursor()
        check = cur.execute(sql_request)
        conn.commit()

        cur.close()
        conn.close()
        logging.info(f'Sql request : {check}')
        is_send =  check == None
        return is_send

    def make_set_for_update(self,list_col,dict_value):
        good_col_format = []

        for key,value in dict_value.items():
            if key in list_col and value != '':
                if key in self.conf.columns_text:
                    good_col_format.append(f"{key}='{self.apply_formatage_type(value)}'")
                else:
                    good_col_format.append(f"{key}={self.apply_formatage_type(value)}")
            elif key in list_col and value =='':
                if key in ['city_id']:
                    good_col_format.append(f"{key}=NULL")
        return ",".join(good_col_format)

    def make_condition_columns(self,dict_column_filtre):
        ''' Auto generate where condition 
            dict_column_filtre  = { 'name_column' : [operator,condition,value,type]}
            operateur:
                OR
                AND 
            condition :
                < : inférieur
                > : supérieur
                <= : inférieur ou égale 
                >= : supérieur ou égale 
                = : égale à
                >< : entre -> value = [borne inférieur,borne supérieur]
                <> : exterieur -> value = [borne inférieur,borne supérieur]
                >=<= : entre Inclusion des bornes -> value = [borne inférieur,borne supérieur]
                <=>= : entre Inclusion des bornes -> value = [borne inférieur,borne supérieur]
                IS : EST
                IN : dans
            type :
            TEXT : for text value
        
        '''
        if dict_column_filtre:
            sql_cond = ['Where']
            for col, param in dict_column_filtre.items():
                
                operator = param[0] if sql_cond != ['Where'] else ''
                condition = param[1]
                value = param[2]
                
                op = 'AND' if condition in  ['><','>=<='] else 'OR'
    
                if param[3] == 'TEXT':
                    if condition in  ['><','<>']:
                
                        sql_cond.append(f"{operator} ({col} {condition[0]} '{value[0]}' {op} {col} {condition[1]} '{value[1]}')")
                    elif condition in ['>=<=','<=>=']:
                    
                        sql_cond.append(f"{operator} ({col} {condition[:2]} '{value[0]}' {op} {col} {condition[2:]} '{value[1]}')")
                    elif condition in ['IS']:
                        sql_cond.append(f"{operator} ({col} {condition} '{value}')")
                    elif condition in ['IN'] and isinstance(value,list):
                        values = ','.join([f"'{val}'" for val in value])
                        sql_cond.append(f"{operator} ({col} {condition} ({values}))")
                    else:
            
                        sql_cond.append(f"{operator} ({col} {condition} '{value}')")


                elif condition in  ['><','<>']:
                    sql_cond.append(f"{operator} ({col} {condition[0]} {value[0]} {op} {col} {condition[1]} {value[1]})")
                elif condition in ['>=<=','<=>=']:
                    sql_cond.append(f"{operator} ({col} {condition[:2]} {value[0]} {op} {col} {condition[2:]} {value[1]})")
                elif condition in ['IS']:
                    sql_cond.append(f"{operator} ({col} {condition} {value})")
                elif condition in ['IN'] and isinstance(value,list):
                        values = ','.join([f"{val}" for val in value])
                        sql_cond.append(f"{operator} ({col} {condition} ({values}))")
                else:
                    sql_cond.append(f"{operator} ({col} {condition} {value})")

            return ' '.join(sql_cond)
        return ''
