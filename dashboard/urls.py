# dashboard/urls.py
from django.urls import include,path


from .views import TrustList, TrustDetail, SchoolList, SchoolDetail
from rest_framework import routers

app_name = 'dashboard'
urlpatterns = [
    path('trusts/', TrustList.as_view(), name='trust-list'),
    path('trusts_detail/<int:pk>/', TrustDetail.as_view(), name='trust-detail'),
    path('schools_list/', SchoolList.as_view(), name='school-list'),
     path('schools_detail/<int:pk>/', SchoolDetail.as_view(), name='school-detail'),
    
     
]                                                                                      