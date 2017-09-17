'''
Created on 16-Sep-2017

@author: tanumoy
'''
from django.views.generic.base import View


class DataEntryTemplate(View):
    def __init__(self, **kwargs):
        View.__init__(self, **kwargs)