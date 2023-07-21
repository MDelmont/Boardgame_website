
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import request
from data.database.tables.liste_table.table_theme import Table_theme
def import_endpoint_theme(app):

    @app.route('/theme/add',methods=['post'])
    def api_add_theme():
        theme = request.get_json(force=True) 

        is_send, id =Table_theme(app).add_value_in_table_with_id_and_unique(theme)

        return {


            'is_send':is_send,
            'id': id
        }

    # @app.route('/theme/update',methods=['post'])
    # def api_update_theme():
    #     theme = request.get_json(force=True) 

    #     pass

    # @app.route('/theme/delete',methods=['post'])
    # def api_delete_theme():
    #     theme = request.get_json(force=True) 

    #     pass

    # @app.route('/theme/<id>',methods=['get'])
    # def api_get_theme_with_id(id):
    #     pass
