
#!/usr/bin/env python
# -*- coding: utf-8 -*-
from data.database.tables.liste_table.table_consumer_have_boardGame import Table_consumer_have_boardgame
from flask import request
def import_endpoint_consumer_boardgame(app):

    @app.route('/consumer_boardgame/add',methods=['post'])
    def api_add_consumer_boardgame():

        consumer_boardgame = request.get_json(force=True) 
        succes = Table_consumer_have_boardgame(app).add_values_in_table(consumer_boardgame)

        return {
                    'is_send' : succes
                }

    # @app.route('/boardgame/update',methods=['post'])
    # def api_update_boardgame(boardgame):

    #     succes = Table_boardgame(app).update_values_in_table(boardgame)

    #     return {
    #                 'Update' : succes
    #             }

    # @app.route('/boardgame/delete/<id>',methods=['post'])
    # def api_delete_boardgame(id):
    #     dict__where = {'id':id}
    #     succes = Table_boardgame(app).del_values_in_table(dict__where)
    #     return {
    #                 'Delete' : succes
    #             }

    # @app.route('/boardgame/<id>',methods=['get'])
    # def api_get_with_id(id):
    #     pass