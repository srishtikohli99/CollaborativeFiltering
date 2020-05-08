import numpy as np
import pandas as pd
import pickle
import os 
dir_path = os.path.dirname(os.path.realpath(__file__))
mod = open(os.path.join(dir_path,'savefile.pickle'), 'rb')
final_model=pickle.load(mod)
items=np.load(os.path.join(dir_path,"items.npy"),allow_pickle=True)
user_to_product_interaction_matrix=open(os.path.join(dir_path,"user_to_product_interaction_matrix"),'rb')
user_to_product_interaction_matrix = pickle.load(user_to_product_interaction_matrix)
mod = open(os.path.join(dir_path,'user2index_map.pickle'), 'rb')
user2index_map=pickle.load(mod)

class recommendation_sampling:
    
    def __init__(self, model, items = items, user_to_product_interaction_matrix = user_to_product_interaction_matrix, 
                user2index_map = user2index_map):
        
        self.user_to_product_interaction_matrix = user_to_product_interaction_matrix
        self.model = model
        self.items = items
        self.user2index_map = user2index_map
    
    def recommendation_for_user(self, user):
        
        # getting the userindex
        rec_items=[]
        
        userindex = self.user2index_map.get(user, None)
        
        if userindex == None:
            return None
        
        users = [userindex]
        
        # products already bought
        
        known_positives = self.items[self.user_to_product_interaction_matrix.tocsr()[userindex].indices]
        
        # scores from model prediction
        scores = self.model.predict(user_ids = users, item_ids = np.arange(self.user_to_product_interaction_matrix.shape[1]))
        
        # top items
        
        top_items = self.items[np.argsort(-scores)]
        
        # printing out the result
        print("User %s" % user)
        print("     Known positives:")
        for x in known_positives[:3]:
            print("                  %s" % x)
            
            
        print("     Recommended:")
        
        for x in top_items[:5]:
            rec_items.append(x)
            print("                  %s" % x)
        return str(rec_items)    
        # return rec_items


recom = recommendation_sampling(model = final_model)
