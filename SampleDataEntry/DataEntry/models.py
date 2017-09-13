from __future__ import unicode_literals

from django.db import models
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref


# Create your models here.
Base = declarative_base()


class Companies(Base):
    __tablename__ = 'companies'
    id = Column('id', Integer, primaary_key=True, autoincrement=True)
    name = Column('name', String(50))
    
    def __init__(self,name):
        self.name = name
        
    def __str__(self):
        return u"Company Name (%s)" % (self.name)
    
    def __repr__(self):
        return u"Company Name (%s)" % (self.name)
    
    
    
class Company_Factors(models.Model):
    __tablename__ = 'company_factors'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    company_id = Column('company_id', Integer, ForeignKey('companies.id'))
    company = relationship('Companies', primaryjoin = 'Companies.id == Company_Factors.company_id')