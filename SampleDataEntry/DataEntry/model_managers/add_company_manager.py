'''
Created on Sep 19, 2017

@author: ibm
'''
from DataEntry.model_managers.db_helper import DBFactory
from DataEntry.models import Companies


def addCompany(companyName):
    factory = DBFactory('dataentry')
    session = factory.getDBSession()
    company = Companies(companyName)
    session.add(company)