
#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import request
from data.database.tables.liste_table.table_mechanic import Table_mechanic
def import_endpoint_mechanic(app):

    @app.route('/mechanic/add',methods=['post'])
    def api_add_mechanic():
        mechanic = request.get_json(force=True) 

        is_send, id = Table_mechanic(app).add_value_in_table_with_id_and_unique(mechanic)

        return {


            'is_send':is_send,
            'id': id
        }

    # @app.route('/mecanique/update',methods=['post'])
    # def api_update_mecanique(boardgame):

    #     pass

    # @app.route('/mecanique/delete',methods=['post'])
    # def api_delete_mecanique(boardgame):

    #     pass

    # @app.route('/mecanique/<id>',methods=['get'])
    # def api_get_mecanique_with_id(id):
    #     pass

