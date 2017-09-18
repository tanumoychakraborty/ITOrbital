'''
Created on 17-Sep-2017

@author: tanumoy
'''

import sqlalchemy




def createDBEngine():
    engine = sqlalchemy.create_engine("postgresql://tanumoy:password@localhost/dataentry", echo=True)
    return engine

