'''
Created on Sep 19, 2017

@author: ibm
'''
from django.http.response import HttpResponse
from django.template import loader
from django.views.decorators.http import require_http_methods

from DataEntry.views.data_entry_template_view import DataEntryTemplate


@require_http_methods(['POST'])
class AddCompanyDataView(DataEntryTemplate):
    
    def post(self, request):
        companyDetails = request.POST.get('companyDetails')

        request.session = {
            }
        template = loader.get_template('DataEntry/home.html')           
        return HttpResponse(template.render(request.session, request))
    

class AddCompanyDataFormView(DataEntryTemplate):
    
    def get(self, request):

        request.session = {
            }
        template = loader.get_template('DataEntry/home.html')           
        return HttpResponse(template.render(request.session, request))