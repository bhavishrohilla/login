from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


def AdminHomeView(request): 
    return render(request, 'currentemployee.html') 


# GOOD NIGHT ALL PROBLEM SOLVED
# change hms landing and login page 
# for a bignner login system take 3 to 7 days 
# congrats you do it within 3 hour
# 3:00 am correct
# its not your fault this is not an easy task
