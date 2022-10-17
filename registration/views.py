from django.shortcuts import render, redirect
from .forms import RegistrationForm
from .models import Registration

# Create your views here.

# create employee

def insert_role(request):
    if request.method == 'POST':
        roleId = request.POST['roleid']
        roleName = request.POST['rolename']

        data = Registration(roleid=roleId, rolename=roleName)
        data.save()

        return redirect('show-role/')
    else:
        return render(request, 'insert-role.html')