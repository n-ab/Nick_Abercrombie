from __future__ import unicode_literals
from django.db import models

import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User_manager(models.Manager):
    def user_manager(self, postData):
        print('----------VALIDATING----------')
        errors = {}
        if len(postData['name']) < 1:
            errors["name"] = "Name required"

        if len(postData['alias']) < 1:
            errors["alias"] = "Alias required"

        if len(postData['email']) < 1:
            errors["email"] = "Email required"

        if len(postData['rpassw']) < 1:
            errors["email"] = "Email required"
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = 'Rethink your email submission!'
        else:
            print '--------------APPROVED------------'
            self.create(name = postData['name'], alias = postData['alias'], email=postData['email'], password=postData['rpassw'])

        return errors

    def login_validator(self, postData):
        print '--------FETCHING DATA---------'
        errors = {}
        user_check = self.filter(email=postData['email'])
        if user_check:
            myuser = user_check[0]
        else:
            errors["email"] = "Your email is not in our system."
        if myuser.password == postData['lpassw']:
            pass
        else:
            errors["lpassw"] = "Your password is incorrect."


        return errors

class User(models.Model):
    name = models.CharField(max_length=255)
    alias = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = User_manager()


class Book_manager(models.Manager):
    def book_manager(self, postData):
        print('---------------VALIDATING BOOK------------')
        errors = {}
        if len(postData['title']) < 1:
            errors["title"] = "Title required"
        if len(postData['author']) < 1:
            errors["author"] = "author required"
        if len(postData['review']) < 1:
            errors["review"] = "review required"
        else:
            print('----------ADDING BOOK------------')
            # self.create(title = postData['title'], author=postData['author'], review=postData['review'])

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    review = models.TextField(default="A nice message.")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = Book_manager()
