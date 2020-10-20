from django.urls import path,include
from django.contrib.auth import views as auth_view
from django.views.generic import TemplateView
from crmapp.views import adminV,Employee,dashboard


urlpatterns = [
    path('',dashboard.home,name='home'),
    path('admin/', include(([
        path('',adminV.AdminHomeView,name='admin-home'),
    ], 'dashboard'),namespace='admin_view')),
     
    path('employee/', include(([     
        path('', Employee.EmployeeHomeView,name='employee-home'),
    ], 'dashboard'),namespace='employee_view')),

]