from __future__ import unicode_literals

from django.db import models
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy.ext.declarative import declarative_base


# Create your models here.

Base = declarative_base()


class Companies(Base):
    __tablename__ = 'companies'
    id = Column(Integer, primaary_key=True)
    name = Column(String)
    
    def __init__(self,name):
        self.name = name
        
    def __str__(self):
        return u"Company Name (%s)" % (self.name)
    
    def __repr__(self):
        return u"Company Name (%s)" % (self.name)
    
    