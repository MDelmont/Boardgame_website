
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import hashlib
from data.database.tables.liste_table.table_consumer import Table_consumer
from data.database.tables.liste_table.table_connexion import Table_connexion
from data.check_data.check_data import Check_data
from flask import Flask
import bcrypt
from flask import request
def import_endpoint_consumer(app):
    table_connexion = Table_connexion(app)

    @app.route('/consumer/add',methods=['post'])
    def api_add_consumer():

        consumers = request.get_json(force=True) 
        succes = Table_consumer(app).add_values_in_table(consumers)

        return {
                    'is_send' : succes
                }

    @app.route('/consumer/update',methods=['post'])
    def api_update_consumer(consumers):

        succes = Table_consumer(app).update_values_in_table(consumers)

        return {
                    'Update' : succes
                }

    @app.route('/consumer/delete/<id>',methods=['post'])
    def api_delete_consumer(id):
        dict__where = {'id':id}
        succes = Table_consumer(app).del_values_in_table(dict__where)
        return {
                    'Delete' : succes
                }


    # Pas possible de requeter cette table
    # @app.route('/consumer/<id>',methods=['get'])
    # def api_get_consumer_with_id(id):
    #     dict__where = {'id':id}

    #     succes = Table_consumer(app).select_value_in_table()
    #     pass

    @app.route('/consumer/connection',methods=['post'])
    def api_connect_user():
  
        json_file = request.get_json(force=True) 
        print(json_file)
        email = str(json_file['email']).encode('utf8')
        password = str(json_file['password']).encode('utf8')
        session_id = str(json_file['session_id']).encode('utf8')
        print(email)
        is_valid=False
        is_good=False
        is_connect= False

        is_valid = Check_data().check_if_data_is_good_for_request([email,password,session_id])
        if is_valid:
            is_good =Table_consumer(app).check_if_password_is_good(email,password)
            if is_good:
                id =Table_consumer(app).get_id_consumer_in_table(email)
                if id:
                    is_connect = Table_connexion(app).add_update_session_in_connexion(id,session=session_id)

        return {
            'is_connect' :is_connect,
            'password':is_good,
            'is_valid':is_valid
        }

    
    @app.route('/consumer/session/<session_id>',methods=['get'])
    def api_check_if_session_exist(session_id):
        print(session_id)
        is_valid = Check_data().check_if_data_is_good_for_request([session_id])
        session_exist = True

        if is_valid :
            session_exist = table_connexion.get_session_exist_in_table(session_id)
            print(session_exist)
            return {"session_id":session_id,
                    "exist" :session_exist,
                    "is_valid" :is_valid
            }
        else:
            return {"session_id":session_id,
                    "is_valid" :is_valid
            }



    @app.route('/consumer/inscription',methods=['post'])
    def api_inscription():
      
        json_file = request.get_json(force=True) 
        email = json_file['email']
        password = json_file['password']
        session_id = json_file['session_id']

        is_valid = Check_data().check_if_data_is_good_for_request([email,password,session_id])

        if is_valid:
            is_send,id =Table_consumer(app).add_consumer_in_table(email,password)
            if is_send and id :
                is_send_session = Table_connexion().add_update_session_in_connexion(id,session_id)
        

        return {
            'creat_user':is_send,
            'connexion_user':is_send_session,
        }

    