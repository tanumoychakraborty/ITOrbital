'''
Created on Sep 19, 2017

@author: ibm
'''
from django.http.response import HttpResponse
from django.template import loader

from DataEntry.model_managers.add_factor_manager import addFactor
from DataEntry.views.data_entry_template_view import DataEntryTemplate


class AddFactorFormView(DataEntryTemplate):
    
    def get(self, request):
        request.session = {
            }
        template = loader.get_template('DataEntry/home.html')           
        return HttpResponse(template.render(request.session, request))
    

class AddFactorView(DataEntryTemplate):
    
    def get(self, request, factor):
        addFactor(factor)
        request.session = {
            }
        template = loader.get_template('DataEntry/home.html')           
        return HttpResponse(template.render(request.session, request))