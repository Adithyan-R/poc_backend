from rest_framework import viewsets, permissions
from .models import EmployeeModel
from .serializers import EmployeeSerializer

class EmployeeViewset(viewsets.ModelViewSet):
    serializer_class = EmployeeSerializer
    permission_classes = [ permissions.IsAuthenticated]
    #lookup_field = "id"

    def get_queryset(self):
        return self.request.user.employee.all()    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


