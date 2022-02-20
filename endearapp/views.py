import datetime
from django.shortcuts import render
from django.http import JsonResponse
from endearapp.models import CrushModel

def home(request):
    context = {}
    return render(request, 'index.html', context)

def dashboard(request):
    context = {}
    return render(request, 'dashboard.html', context)

def add_crush(request):
    if request.method == 'POST':
        response_data = {"name": request.POST.get('name'), "email": request.POST.get('email')}
        crush_model = CrushModel.objects.create(
            original_user = request.user,
            crush_name = response_data['name'],
            crush_email = response_data['email'],
            record_date = datetime.datetime.now())
        
        crush_model.save()
    return JsonResponse(response_data, status=201)
