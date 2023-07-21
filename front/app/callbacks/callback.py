
from callbacks import callback_barre_menu,callback_boardgame_card,callback_page_jeux,callback_page_profil,callback_session,callback_page_suggestion,callback_connexion
def import_all_callback(app):
    callback_barre_menu.import_all_callback_barre_menu(app)
    callback_boardgame_card.import_all_callback_boardgame_card(app)
    callback_page_jeux.import_all_callback_page_jeux(app)
    callback_page_profil.import_all_callback_page_profil(app)
    callback_session.import_all_callback_session_id(app)
    callback_page_suggestion.import_all_callback_page_suggetion(app)
    callback_connexion.import_all_callback_connexion(app)

