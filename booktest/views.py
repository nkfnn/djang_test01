from django.shortcuts import render,redirect
from django.http import JsonResponse

# Create your views here.
def index(request):
    return render(request,'booktest/index.html')

def login(request):
    return render(request,'booktest/login.html')

def login_check(requset):
    # 1获取参数
    username = requset.POST.get('username')
    # print(username)
    password = requset.POST.get('password')
    # print(password)
    # 2判断密码是否正确
    if username == 'python':
        return redirect('/index')
    else:
        return redirect('/login')

def login_ajax(request):
    return render(request,'booktest/login_ajax.html')

def login_ajax_check(request):

    username = request.POST.get('username')
    print('----------->',username)
    # print(username)
    password = request.POST.get('password')
    print('----------->',password)
    if username == 'python':
        return JsonResponse({'res':1})
    else:
        return JsonResponse({'res':2})
