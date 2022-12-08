
from rest_framework import routers

from django.urls import path, include
from .api import EmployeeViewset

app_name = "api"
router = routers.DefaultRouter()
router.register('employee',EmployeeViewset,basename='employee')

urlpatterns = [
    path('', include(router.urls)),
]












'''
from django.urls import path
from .api import EmployeeList, EmployeeDetail



urlpatterns = [
    path('employee', EmployeeList.as_view(),name="employees"),
    #?P<id>.*)$
    path('employee/<int:pk>', EmployeeDetail.as_view(), name="employee"),
]



urlpatterns = [
    path('edit/<int:pk>', EmployeeViewset.as_view()),
    path('delete/<int:pk>', EmployeeViewset.as_view())
]

'''