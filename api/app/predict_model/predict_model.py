
import pickle 
from sklearn.neighbors import NearestNeighbors
import pandas as pd
import json
class predict_model():
    def __init__(self):
        self.model = self.load_model_predict()
        self.line_to_id_board = self.loard_line_to_id_board()
        self.df_model = self.load_df_model()

    def load_model_predict(self):
        return pickle.load(open('./api/data/model/model', 'rb'))

    def load_df_model(self):
        return pd.read_csv('./api/data/model/df_model.csv')
    
    def loard_line_to_id_board(self):
        return json.load(open('./api/data/model/line_to_id_board.json'))

    def predict_model(self,list_id):
        dict_list_id = {}
        for id in list_id:
            distances, indices = self.model.kneighbors( self.df_model.loc[id:id])
            for id_pred in  [ self.line_to_id_board[key] for key in indices[0]]:
                if id_pred in dict_list_id.keys():
                    dict_list_id[id_pred]+=1
                else:
                    dict_list_id[id_pred]=1
        return dict_list_id






