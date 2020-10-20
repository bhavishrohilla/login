from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

def EmployeeHomeView(request):
     return render(request, 'currentemployee.html') 
