from rest_framework import viewsets, permissions
from .models import EmployeeModel
from .serializers import EmployeeSerializer
from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView

class EmployeeViewset(viewsets.ModelViewSet):
    serializer_class = EmployeeSerializer
    permission_classes = [ permissions.IsAuthenticated]
    #lookup_field = "id"

    def get_queryset(self):
        return EmployeeModel.objects.all()     #filter(owner=self.request.user)#pk=self.lookup_url_kwarg  
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)











'''
class EmployeeList(ListCreateAPIView):
    """
    List all employees, or create a new employee.
    """

    serializer_class = EmployeeSerializer
    permission_classes = (permissions.IsAuthenticated,)


    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        return super().perform_create(serializer)

    def get_queryset(self):
        return EmployeeModel.objects.filter(owner=self.request.user,pk=self.lookup_url_kwarg)



class EmployeeDetail(RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a employee instance.
    """
    serializer_class = EmployeeSerializer
    permission_classes = (permissions.IsAuthenticated,)
    lookup_field="id"

    def get_queryset(self):
        return EmployeeModel.objects.filter(owner=self.request.user)

'''