'''
Created on 12-Sep-2017

@author: tanumoy
'''
from django.db import models

class check_login(models.Manager):
    def create_user(self,username,password):
        login = self.create(username=username, password=password)
        return login
    
    def check_login(self, username,password):
        