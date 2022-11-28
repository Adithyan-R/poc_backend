from rest_framework import routers

from .api import EmployeeViewset

router = routers.DefaultRouter()
router.register('employee', EmployeeViewset, 'employee')


urlpatterns = router.urls