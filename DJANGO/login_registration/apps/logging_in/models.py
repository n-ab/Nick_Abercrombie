# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import re
from django.db import models
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

class UserManager(models.Manager):
    def validate_user(self, post_data):
        print '_____________________'
        errors = {}
        if len(post_data['first_name']) > 2:
            print 'First Name Looks Good!'
        else:
            errors["first_name"] = "First name cannot be empty"
        if len(post_data['last_name']) >2 :
            print 'Last name looks good!'
        else: 
            errors["last_name"] = "Last name cannot be empty"
        if post_data['password'] == post_data['confirm']:
            print('They match')
        else:
            errors['password'] = "Passwords must match"
        if not EMAIL_REGEX.match(post_data['email']):
            errors['email'] = 'Rethink your email submission!'
        else:
            print 'everything looks great! add to system!'
            self.create(first_name = post_data['first_name'], last_name = post_data['last_name'], email=post_data['email'], password=post_data['password'])

        return errors

    def login_validator(self, post_data):
        print '_______ISTHISWORKING?????'
        errors = {}
        user_check = self.filter(email=post_data['email'])
        if user_check:
            myuser = user_check[0]
        else:
            errors["email"] = "Your email is not in our system."
        if myuser.password == post_data['password']:
            pass
        else:
            errors["password"] = "Your password is incorrect."

        
        return errors
    

class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length = 30)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length = 10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    objects = UserManager()
