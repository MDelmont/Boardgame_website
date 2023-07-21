from data.database.tables.liste_table.table_boardgame import Table_boardgame
from data.database.tables.liste_table.table_consumer import Table_consumer
from data.database.tables.liste_table.table_mechanic import Table_mechanic
from data.database.tables.liste_table.table_theme import Table_theme
from data.database.tables.liste_table.table_boardGame_have_mechanic import Table_boardgame_have_mechanic
from data.database.tables.liste_table.table_boardGame_have_theme import Table_boardgame_have_theme
from data.database.tables.liste_table.table_consumer_have_boardGame import Table_consumer_have_boardgame
from data.database.tables.liste_table.table_connexion import Table_connexion


list_table = [

    Table_boardgame('app'),
    Table_consumer('app'),
    Table_mechanic('app'),
    Table_theme('app'),
    Table_boardgame_have_mechanic('app'),
    Table_boardgame_have_theme('app'),
    Table_consumer_have_boardgame('app'),
    Table_connexion('app')

]

# for table in list_table:
#     print( table.name)
#     table.creat_table_if_not_exist()
tlb =  Table_consumer('app')

print(tlb.check_if_password_is_good('matthieu@delmon.fr','1234boardgame'))