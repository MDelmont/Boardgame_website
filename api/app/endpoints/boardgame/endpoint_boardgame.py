
#!/usr/bin/env python
# -*- coding: utf-8 -*-
from data.database.tables.liste_table.table_boardgame import Table_boardgame
from flask import request
def import_endpoint_boardgame(app):

    @app.route('/boardgame/add',methods=['post'])
    def api_add_boardgame():
        boardgame = request.get_json(force=True) 

        is_send, id_board_game= Table_boardgame(app).add_value_in_table_with_id_and_unique(boardgame)

        return {    
                    
                    'is_send' : is_send,
                    'id':id_board_game,
                }

    @app.route('/boardgame/update',methods=['post'])
    def api_update_boardgame(boardgame):

        succes = Table_boardgame(app).update_values_in_table(boardgame)

        return {
                    'Update' : succes
                }

    @app.route('/boardgame/delete/<id>',methods=['post'])
    def api_delete_boardgame(id):
        dict__where = {'id':id}
        succes = Table_boardgame(app).del_values_in_table(dict__where)
        return {
                    'Delete' : succes
                }

    @app.route('/boardgame/<id>',methods=['get'])
    def api_get_with_id(id):
        pass