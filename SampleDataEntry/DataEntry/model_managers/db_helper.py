'''
Created on 17-Sep-2017

@author: tanumoy
'''

import sqlalchemy, sqlalchemy.orm
from sqlalchemy.ext.declarative.api import declarative_base


class DBFactory:
    __session = {}
    __base = {}
    __dataentryConnectionString = 'postgresql://tanumoy:password@localhost/dataentry'
    
    def __init__(self, db):
        self.__db = db
    
    def __getConnectionString(self):
        return {'dataentry': self.__dataentryConnectionString,
                }[self.__db]
        
    
    def __createDBEngine(self):
        engine = sqlalchemy.create_engine(self.__getConnectionString(), echo=True)
        return engine
    
    def __createBase(self):
        Base = declarative_base()        
        Base.metadata.bind = self.__createDBEngine()
        self.__base.update({self.__db : Base})
    
    def __createDBession(self):
        engine = self.__createDBEngine()
        Session = sqlalchemy.orm.sessionmaker(bind=engine)
        session = Session()
        self.__session.update({self.__db : session})
    
    def getDBSession(self):
        if(self.__db not in self.__session.iterkeys()):
            self.__createDBession()
            print "##############################CREATING DB SESSION ######################################"
        return self.__session.get(self.__db)
    
    def getDBBase(self):
        if(self.__db not in self.__base.iterkeys()):
            self.__createBase()
        return self.__base.get(self.__db)



def getFactors(factor):
    header = factor.__table__.columns.keys()
    header.remove('id')
    header.remove('company_id')
    return header