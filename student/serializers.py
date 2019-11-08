from rest_framework import serializers
from .models import Student, College


class StudentSerializer(serializers.ModelSerializer):

   class Meta:
       model = Student
       fields = '__all__'


class CollegeSerializer(serializers.ModelSerializer):

   class Meta:
       model = College
       fields = '__all__'
