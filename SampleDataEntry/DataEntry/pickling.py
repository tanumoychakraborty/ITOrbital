'''
Created on 14-Sep-2017

@author: tanumoy
'''
import os
import pickle


def save_factors(factors):
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),"factors")
    with open (path, 'wb') as fp:
        pickle.dump(factors,fp)
        

def get_factors():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),"factors")
    with open (path, 'rb') as fp:
        factors = pickle.load(fp)
        
    return factors