'''
Created on 16-Sep-2017

@author: tanumoy
'''
from django.http.response import HttpResponse
from django.template import loader
import sqlalchemy.orm

from SampleDataEntry.DataEntry.views.data_entry_template_view import DataEntryTemplate
from SampleDataEntry.SampleDataEntry import settings
from SampleDataEntry.DataEntry.models import Companies


class HomeView(DataEntryTemplate):
    
    def get(self, request):
        
        engine = sqlalchemy.create_engine(settings.DATABASES['default']['NAME'], echo=True)
        Session = sqlalchemy.orm.sessionmaker(bind=engine)
        session = Session()
        #Base.metadata.create_all(engine)
        companies = session.query(Companies).all()
        
        request.session = {
            'companies' : companies,
            }
        template = loader.get_template('dashboard/detailed_automation_report.html')           
        return HttpResponse(template.render(request.session, request))