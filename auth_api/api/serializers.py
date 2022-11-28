from rest_framework import serializers
from api.models import EmployeeModel

class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = EmployeeModel
        fields = ['name','id','department','designation','phonenumber']

