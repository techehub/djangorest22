from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import StudentList, StudentDetail, ColleageList, CollegeDetail

urlpatterns = [
   path('students/', StudentList.as_view()),
   path('students/<int:pk>/', StudentDetail.as_view()),
   path('colleges/', ColleageList.as_view()),
   path('colleges/<int:pk>/', CollegeDetail.as_view()),
]
