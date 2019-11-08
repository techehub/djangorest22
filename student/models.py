from django.db import models

# Create your models here.

class College(models.Model):
   created = models.DateTimeField(auto_now_add=True)
   name = models.CharField(max_length=100, blank=True, default='')
   address = models.CharField(max_length=100, blank=True, default='')
   phone = models.CharField(max_length=100, blank=True, default='')

   class Meta:
       ordering = ('created',)

   def __str__(self):
       return self.name



class Student(models.Model):
   created = models.DateTimeField(auto_now_add=True)
   firstname = models.CharField(max_length=100, blank=True, default='')
   lastname = models.CharField(max_length=100, blank=True, default='')
   address = models.CharField(max_length=100, blank=True, default='')
   phone = models.CharField(max_length=100, blank=True, default='')
   colleage = models.ForeignKey(College, on_delete= models.CASCADE, default='')

   class Meta:
       ordering = ('created',)

   def __str__(self):
       return self.title