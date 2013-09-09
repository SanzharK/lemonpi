from django.db import models

# Create your models here.
# After we make any changes to our Model class we need to run the command
# 'python manage.py syncdb' for the changes to take place
# First of all I'm going to concentrate on just the user model.
class User(models.Model):
    name = models.CharField(max_length=100, blank=True, default='')
    surname = models.CharField(max_length=100, blank=True, default='')

    class Meta: #here we can change various settings about the model
        ordering = ('name',) # order them by name
