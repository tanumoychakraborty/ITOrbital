'''
Created on Sep 19, 2017

@author: ibm
'''
from DataEntry.model_managers.db_helper import DBFactory, getColumnWithType


def addFactor(factorName):
    factory = DBFactory('dataentry')
    engine = factory.getDBEngine()
    
    column = getColumnWithType(type, factorName)
    column_name = column.compile(dialect=engine.dialect)
    column_type = column.type.compile(engine.dialect)
    engine.execute('ALTER TABLE %s ADD COLUMN %s %s' % (factorName, column_name, column_type))
    
#     column_name = column.compile(dialect=engine.dialect)
#     column_type = column.type.compile(engine.dialect)
#     engine.execute('ALTER TABLE %s ADD COLUMN %s %s' % (table_name, column_name, column_type))
# 
#     column = Column('new column', String(100), primary_key=True)
#     add_column(engine, table_name, column)