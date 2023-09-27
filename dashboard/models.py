# from django.db import models
# dashboard/models.py
from django.db import models
from django.contrib.auth.models import User
import bcrypt

class Trust(models.Model):
    name = models.CharField(max_length=100)
    user = models.ManyToManyField(User, related_name='trusts')

    def __str__(self):
        return self.name

class School(models.Model):
    name = models.CharField(max_length=100)
    domain_url = models.URLField()
    login_user = models.CharField(max_length=100, default='default_value_here')
    login_password = models.CharField(max_length=100)
    email =models.EmailField(max_length=100,default='example@gmail.com')
    trust = models.ForeignKey(Trust, on_delete=models.CASCADE, related_name='schools')
    
    def __str__(self):
        return self.name

    # def save(self, *args, **kwargs):
    # # Check if the login_password is not hashed
    #  if not self.login_password.startswith('$2b$'):
    #     # Hash the login_password
    #     hashed_password = bcrypt.hashpw(self.login_password.encode('utf-8'), bcrypt.gensalt())
    #     self.login_password = hashed_password.decode('utf-8')

    #  super(School, self).save(*args, **kwargs)
    def save(self, *args, **kwargs):
    # Check if the login_user is not hashed
     

    # Hash the login_password if it's not already hashed
     if not self.login_password.startswith('$2b$'):
        hashed_password = bcrypt.hashpw(self.login_password.encode('utf-8'), bcrypt.gensalt())
        self.login_password = hashed_password.decode('utf-8')

     super(School, self).save(*args, **kwargs)



