
from django.shortcuts import render, HttpResponse, redirect, reverse
from django.contrib.auth import authenticate, login as auth_login
from .models import TreatmentInfo, PatientRecords, MedicalHistory

# Create your views here.
 
# 主界面
def index(request):
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
                    return render(request, 'index.html')
 
            else:
                context = {
                    'aa': '用户名密码错误'
                }
                return redirect(request, 'login.html', context)
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
 