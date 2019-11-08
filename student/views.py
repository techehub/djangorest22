
from rest_framework import generics
from .models import Student, College
from .serializers import StudentSerializer, CollegeSerializer

class StudentList(generics.ListCreateAPIView):
  queryset = Student.objects.all()
  serializer_class = StudentSerializer


class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Student.objects.all()
  serializer_class = StudentSerializer


class ColleageList(generics.ListCreateAPIView):
  queryset = College.objects.all()
  serializer_class = CollegeSerializer


class CollegeDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = College.objects.all()
  serializer_class = CollegeSerializer
