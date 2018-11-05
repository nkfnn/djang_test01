from django.shortcuts import render,redirect
from django.http import JsonResponse

# Create your views here.
def index(request):

    return render(request,'booktest/index.html')

def login(request):
    # 判断是否已经登录
    if request.session.has_key('islogin'):
        return redirect('/index')
    else:
        if 'username' in request.COOKIES:
            username = request.COOKIES['username']
        else:
            username = ''
        return render(request,'booktest/login.html',{'username':username})

def login_check(request):
    # 1获取参数
    username = request.POST.get('username')
    # print(username)
    password = request.POST.get('password')
    remeber = request.POST.get('remeber')
    # print(remeber)
    # print(password)
    # 2判断密码是否正确
    if username == 'pythonn':
        response = redirect('/index')
        # 判断是否需要记住用户名
        if remeber == 'on':
            response.set_cookie('username',username,max_age=7*24*3600)
        # 设置登录
        request.session['islogin']=True

        return response
    else:
        return redirect('/login')

def login_ajax(request):
    return render(request,'booktest/login_ajax.html')

def login_ajax_check(request):

    username = request.POST.get('username')
    # print('----------->',username)
    # print(username)
    password = request.POST.get('password')
    # print('----------->',password)
    if username == 'python':
        return JsonResponse({'res':1})
    else:
        return JsonResponse({'res':2})


