from __future__ import unicode_literals

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship, backref
from sqlalchemy.sql.schema import ForeignKeyConstraint
from DataEntry.model_managers.db_helper import DBFactory


# Create your models here.
db = 'dataentry'
factory = DBFactory(db)
Base = factory.getDBBase()

class Companies(Base):
    __tablename__ = 'companies'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    name = Column('name', String(50), nullable=False)
    
    def __init__(self, name):
        self.name = name
        
    def __str__(self):
        return u"Company Name (%s)" % (self.name)
    
    def __repr__(self):
        return u"Company Name (%s)" % (self.name)
    

class Factors(Base):
    __tablename__ = 'factors'
    __table_args__ = (ForeignKeyConstraint(['company_id'], ['companies.id']), {'autoload':True})
    company = relationship('Companies', backref= backref('Factors', lazy='dynamic'))
    
