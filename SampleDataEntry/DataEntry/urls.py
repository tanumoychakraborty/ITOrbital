'''
Created on 16-Sep-2017

@author: tanumoy
'''


from django.conf.urls import url

from DataEntry.views.home_view import HomeView


urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
]
