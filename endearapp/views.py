import datetime
from django.shortcuts import render
from django.shortcuts import redirect
from endearapp.models import CrushModel

def home(request):
    context = {}
    return render(request, 'index.html', context)

def dashboard(request):
    context, crushes = {}, {}
    user_crushes = CrushModel.objects.filter(original_user=request.user).values('crush_name','crush_email')
    for crush in user_crushes:
        crushes[crush['crush_name']] = crushes.get(crush['crush_name'], crush['crush_email'])
    if request.method == 'POST':
        if 'delete' in request.POST:
            CrushModel.objects.filter(crush_email__iexact=request.POST.get('delete')).delete()
            return redirect('/dashboard/')
        elif 'name' in request.POST and 'email' in request.POST:
            if request.POST.get('name') in crushes:
                pass
            if len(user_crushes) < 3: 
                response_data = {"name": request.POST.get('name'), "email": request.POST.get('email')}
                crush_model = CrushModel.objects.create(
                    original_user = request.user,
                    crush_name = response_data['name'],
                    crush_email = response_data['email'],
                    record_date = datetime.datetime.now())
                crush_model.save()
                return redirect('/dashboard/')
            else:
                context['crushes'] = crushes
                return render(request, 'dashboard.html', context)
        else:
            return render(request, 'dashboard.html', context)
    else:
        context['crushes'] = crushes
    return render(request, 'dashboard.html', context)

def solution(request):
    context = {}
    return render(request, 'solution.html', context)

def login_error(request):
    context = {}
    return render(request, 'error.html', context)
