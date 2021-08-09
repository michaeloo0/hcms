
from django.shortcuts import render, HttpResponse, redirect, reverse
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from .models import TreatmentInfo, PatientRecords, MedicalHistory

# Create your views here.
 
# 主界面
def index(request):
    if not request.user.is_authenticated:
        return render(request, 'index.html')
    
    qs = Group.objects.get(user=request.user)
    if qs.name == 'DOCTOR':
        
        patient_records = PatientRecords.objects.filter(attending=request.user).all()
        context = {'patients':patient_records}
        return render(request, 'doctor-list.html', context=context)
    
    if qs.name == 'AGENCY':
        
        treatment_info = PatientRecords.objects.all()
        context = {'patients':treatment_info}
        return render(request, 'agency-list.html', context=context)
    
    if qs.name == 'ADMIN':
        
        return redirect('http://127.0.0.1:8000/admin')
    
    context = {
        'status': '未登录状态'
    }
    return render(request, 'index.html', context)
 
# 登录界面s
def login(request):
    if request.method == "POST":
        # id = request.POST.get('id')
        username = request.POST.get('username')
        password = request.POST.get('password')
        if not all([username, password]):
            return HttpResponse('参数不全')
        else:
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    auth_login(request, user)
                    return redirect('list')
 
            else:
                context = {
                    'aa': '用户名密码错误'
                }
                return render(request, 'login.html', context)
    else:
        context = {
            'status': '未登录状态',
            'length': 0
        }
        return render(request, 'login.html', context)
 

# 退出界面s
def logout(request):
    # 注销掉用户，从删除session中保存的信息
    request.session.clear()
    return render(request, 'index.html')
 


def common_list(request):
    
    if not request.user.is_authenticated:
        return redirect('login')
 
    qs = Group.objects.get(user=request.user)

    if qs.name == 'DOCTOR':
        
        patient_records = PatientRecords.objects.filter(attending=request.user).all()
        context = {'patients':patient_records}
        print(request.user)
        return render(request, 'doctor-list.html', context=context)
    
    if qs.name == 'AGENCY':
        
        treatment_info = PatientRecords.objects.all()
        context = {'patients':treatment_info}
        return render(request, 'agency-list.html', context=context)
    
    if qs.name == 'ADMIN':
        
        return redirect('http://127.0.0.1:8000/admin')
    
    return render(request, 'index.html')