
#!/usr/bin/env python
# -*- coding: utf-8 -*-
from data.database.tables.liste_table.table_boardGame_have_mechanic import Table_boardgame_have_mechanic
from flask import request
def import_endpoint_boardgame_mechanic(app):

    @app.route('/boardgame_mechanic/add',methods=['post'])
    def api_add_boardgame_mecanic():
        boardgame_mecanic = request.get_json(force=True) 
        succes = Table_boardgame_have_mechanic(app).add_values_in_table(boardgame_mecanic)

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

    @app.route('/mecanic/<id>',methods=['get'])
    def api_get_with_mecanic_id(id):
        pass