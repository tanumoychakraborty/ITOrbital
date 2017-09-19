'''
Created on 16-Sep-2017

@author: tanumoy
'''
from django.http.response import HttpResponse
from django.template import loader
from DataEntry.views.data_entry_template_view import DataEntryTemplate
from DataEntry.model_managers.all_details_manager import getAllData


class HomeView(DataEntryTemplate):
    
    def get(self, request):
        header, payload = getAllData()
        request.session = {
            'header' : header,
            'payload' : payload,
            }
        template = loader.get_template('DataEntry/home.html')           
        return HttpResponse(template.render(request.session, request))