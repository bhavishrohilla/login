from django.shortcuts import redirect, render
from django.views.generic import TemplateView




def home(request):
    if request.user.is_authenticated:
        if request.user.is_admin:
            return redirect('admin_view:admin-home')
        else:
            return redirect('employee_view:employee-home')
    return render(request, 'landing.html')
