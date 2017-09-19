'''
Created on Sep 19, 2017

@author: ibm
'''
from django.http.response import HttpResponse
from django.template import loader

from DataEntry.views.data_entry_template_view import DataEntryTemplate
from DataEntry.model_managers.add_company_manager import addCompany


class AddCompanyFormView(DataEntryTemplate):
    
    def get(self, request):
        request.session = {
            }
        template = loader.get_template('DataEntry/companyAddSuccess.html')           
        return HttpResponse(template.render(request.session, request))
    
class AddCompanyView(DataEntryTemplate):
    
    def get(self, request, company):
        addCompany(company)
        request.session = {
            }
        template = loader.get_template('DataEntry/companyAddSuccess.html')           
        return HttpResponse(template.render(request.session, request))