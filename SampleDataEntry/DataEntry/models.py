from __future__ import unicode_literals

from sqlalchemy import Column, Integer, String
import sqlalchemy, sqlalchemy.orm
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from sqlalchemy.sql.schema import ForeignKeyConstraint

from DataEntry.model_managers.db_helper import createDBEngine


# Create your models here.
#Session = sqlalchemy.orm.sessionmaker(bind=engine)
#session = Session()
#Base.metadata.create_all(engine)
Base = declarative_base()        
Base.metadata.bind = createDBEngine()


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
    
