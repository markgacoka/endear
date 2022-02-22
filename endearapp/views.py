import datetime
from django.shortcuts import render
from django.shortcuts import redirect
from endearapp.models import CrushModel

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
        new_crushes = []
        user_crushes = CrushModel.objects.filter(original_user=request.user).values('crush_name','crush_email')
        for crush in user_crushes:
            crushes[crush['crush_name']] = crushes.get(crush['crush_name'], crush['crush_email'])
        new_crush_model = CrushModel.objects.filter(crush_email=request.user.email).values('original_user_id', 'record_date', 'original_name')
        for email in new_crush_model:
            new_crushes = {email['original_name']: [email['original_user_id'], email['record_date'].strftime('%d-%m-%Y'), email['original_user_id'] in crushes.values()]}
        
        if request.method == 'POST':
            if 'delete' in request.POST:
                CrushModel.objects.filter(crush_email__iexact=request.POST.get('delete')).delete()
                return redirect('/dashboard/')
            elif 'name' in request.POST and 'email' in request.POST:
                if request.POST.get('email') == request.user.email:
                    context['crushes'] = crushes
                    return render(request, 'dashboard.html', context)
                if len(user_crushes) < 3: 
                    response_data = {"name": request.POST.get('name'), "email": request.POST.get('email')}
                    crush_model = CrushModel.objects.create(
                        original_user = request.user,
                        original_name = request.user.first_name + ' ' + request.user.last_name,
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
            context['new_crushes'] = new_crushes
        return render(request, 'dashboard.html', context)

def solution(request):
    context = {}
    return render(request, 'solution.html', context)

def login_error(request):
    context = {}
    return render(request, 'error.html', context)
