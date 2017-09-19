'''
Created on 16-Sep-2017

@author: tanumoy
'''


from django.conf.urls import url

from DataEntry.views.add_company_data_view import AddCompanyDataView, \
    AddCompanyDataFormView
from DataEntry.views.add_company_view import AddCompanyFormView, AddCompanyView
from DataEntry.views.add_factor_view import AddFactorView, AddFactorFormView
from DataEntry.views.home_view import HomeView


urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^AddCompanyForm/$', AddCompanyFormView.as_view(), name='addCompanyForm'),
    url(r'^AddCompany/(?P<company>[a-zA-Z0-9_&]+)$', AddCompanyView.as_view(), name='addCompany'),
    url(r'^AddFactor/(?P<factor>[a-zA-Z0-9_&]+)$', AddFactorView.as_view(), name='addFactor'),
    url(r'^AddFactor/$', AddFactorFormView.as_view(), name='addFactorForm'),
    url(r'^AddDataForm/$', AddCompanyDataFormView.as_view(), name='addDataForm'),
    url(r'^AddData/$', AddCompanyDataView.as_view(), name='addData'),
]
