'''
Created on 19-Sep-2017

@author: tanumoy
'''
from collections import OrderedDict

from DataEntry.model_managers.db_helper import DBFactory, getFactors
from DataEntry.models import Factors


def getAllData():
    factory = DBFactory('dataentry')
    session = factory.getDBSession()
    factors = session.query(Factors).all()
    header = OrderedDict()
    header['company'] = 'Company Name'
    for h in getFactors(factors[0]):
        header[h] = h
#     length = len(factors)+1
    payload =  []
    col_names = factors[0].__table__.columns.keys()
    for factor in factors:
        row = header.copy()
        for name in col_names:
            if name != "id" :
                if name == "company_id" :
                    row['company'] = factor.company.name
                else:
                    row[name] = getattr(factor, name)
        
        payload.append(row)
    
    return header, payload    
    