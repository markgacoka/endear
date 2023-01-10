import datetime
from django.shortcuts import render, redirect
from endearapp.models import CrushModel
import cryptocode

def home(request):
    context = {}
    if request.user.is_authenticated:
        return redirect('/dashboard')
    else:
        return render(request, 'index.html', context)

def dashboard(request):
    if not request.user.is_authenticated:
        return redirect('/')
    else:
        context, crushes = {}, {}
        new_crushes = {}
        user_crushes = CrushModel.objects.filter(original_user=request.user).values('crush_name','crush_email')
        for entry in user_crushes:
            crushes[cryptocode.decrypt(entry['crush_name'], "endear")] = cryptocode.decrypt(entry['crush_email'], "endear")
            
        new_crush_model = CrushModel.objects.all().values_list()
        for _, entry in enumerate(new_crush_model):
            if cryptocode.decrypt(entry[4], 'endear') == request.user.email:
                new_crushes[entry[2]] = new_crushes.get(entry[2], [entry[1], entry[5].strftime('%d-%m-%Y'), True])
        context['crushes_three'] = 'False'
        if request.method == 'POST':
            if 'delete' in request.POST:
                deletion_list = CrushModel.objects.filter(original_user=request.user).values_list()
                for entry in deletion_list:
                    if cryptocode.decrypt(entry[4], 'endear') == request.POST.get('delete'):
                        CrushModel.objects.get(id=entry[0]).delete()
                return redirect('/dashboard/')
            elif 'name' in request.POST and 'email' in request.POST:
                if request.POST.get('email') == request.user.email:
                    context['crushes'] = crushes
                    return render(request, 'dashboard.html', context)
                if request.POST.get('email') in set(crushes.values()):
                    context['crushes'] = crushes
                    return render(request, 'dashboard.html', context)
                if len(user_crushes) < 4: 
                    response_data = {"name": request.POST.get('name'), "email": request.POST.get('email')}
                    crush_model = CrushModel.objects.create(
                        original_user = request.user,
                        original_name = request.user.first_name + ' ' + request.user.last_name,
                        crush_name = cryptocode.encrypt(response_data['name'], "endear"),
                        crush_email = cryptocode.encrypt(response_data['email'], "endear"),
                        record_date = datetime.datetime.now())
                    crush_model.save()
                    return redirect('/dashboard/')
                else:
                    context['crushes_three'] = 'True'
                    context['crushes'] = crushes
                    return render(request, 'dashboard.html', context)
            else:
                return render(request, 'dashboard.html', context)
        else:
            context['crushes'] = crushes
            context['new_crushes'] = new_crushes
        return render(request, 'dashboard.html', context)

def solution(request):
    context = {}
    return render(request, 'solution.html', context)

def war(request):
    context = {}
    return render(request, 'war.html', context)

def login_error(request):
    context = {}
    return render(request, 'error.html', context)
