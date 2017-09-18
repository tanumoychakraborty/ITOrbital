'''
Created on 16-Sep-2017

@author: tanumoy
'''
from django.http.response import HttpResponse
from django.template import loader
import sqlalchemy.orm

from DataEntry.models import Companies, Factors
from DataEntry.views.data_entry_template_view import DataEntryTemplate


class HomeView(DataEntryTemplate):
    
    def get(self, request):
        
        engine = sqlalchemy.create_engine("postgresql://tanumoy:password@localhost/dataentry", echo=True)
        Session = sqlalchemy.orm.sessionmaker(bind=engine)
        session = Session()
        #Base.metadata.create_all(engine)
        factors = session.query(Factors).all()
        for factor in factors:
            print factor.id
            print factor.company.name
        
        request.session = {
            'companies' : factors,
            }
        template = loader.get_template('dashboard/detailed_automation_report.html')           
        return HttpResponse(template.render(request.session, request))