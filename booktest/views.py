from django.shortcuts import render,redirect
from django.http import JsonResponse,HttpResponse

# 登录验证
def login_require(view_func):
    def warpper(request,*args,**kwargs):
        if request.session.has_key('isLogin1'):
            return view_func(request,*args,**kwargs)
        else:
            return redirect('/login1')
    return warpper

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

def login1(request):
    # 首先判断是否已经登录
    if request.session.has_key('isLogin1'):
        return redirect('/index')
    else:
        if 'usern' in request.COOKIES:
            username = request.COOKIES.get('usern')
        else:
            username = ''
        return render(request,'booktest/login1.html',{"username":username})

def login1_check(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    remeber = request.POST.get('remeber')
    # 检测用户名密码是否正确
    if username == "pythonniu":
        response = redirect('/index')
        # 如果remeber为‘on’,设置cookies,
        if remeber == 'on':
            response.set_cookie("usern",username)
        # 设置session
        request.session['isLogin1'] = True
        return response
    else:
        return redirect('/login1')

@login_require
def change_pwd(request):
    content = '123'
    return render(request,'booktest/sucess.html',{"content":content})

from PIL import Image, ImageDraw, ImageFont
from django.utils.six import BytesIO

def verify_code(request):
    #引入随机函数模块
    import random
    #定义变量，用于画面的背景色、宽、高
    bgcolor = (random.randrange(20, 100), random.randrange(
        20, 100), 255)
    width = 100
    height = 25
    #创建画面对象
    im = Image.new('RGB', (width, height), bgcolor)
    #创建画笔对象
    draw = ImageDraw.Draw(im)
    #调用画笔的point()函数绘制噪点
    for i in range(0, 100):
        xy = (random.randrange(0, width), random.randrange(0, height))
        fill = (random.randrange(0, 255), 255, random.randrange(0, 255))
        draw.point(xy, fill=fill)
    #定义验证码的备选值
    str1 = 'ABCD123EFGHIJK456LMNOPQRS789TUVWXYZ0'
    #随机选取4个值作为验证码
    rand_str = ''
    for i in range(0, 4):
        rand_str += str1[random.randrange(0, len(str1))]
    #构造字体对象，ubuntu的字体路径为“/usr/share/fonts/truetype/freefont”
    font = ImageFont.truetype('FreeMono.ttf', 23)
    #构造字体颜色
    fontcolor = (255, random.randrange(0, 255), random.randrange(0, 255))
    #绘制4个字
    draw.text((5, 2), rand_str[0], font=font, fill=fontcolor)
    draw.text((25, 2), rand_str[1], font=font, fill=fontcolor)
    draw.text((50, 2), rand_str[2], font=font, fill=fontcolor)
    draw.text((75, 2), rand_str[3], font=font, fill=fontcolor)
    #释放画笔
    del draw
    #存入session，用于做进一步验证
    request.session['verifycode'] = rand_str
    #内存文件操作
    buf = BytesIO()
    #将图片保存在内存中，文件类型为png
    im.save(buf, 'png')
    #将内存中的图片数据返回给客户端，MIME类型为图片png
    return HttpResponse(buf.getvalue(), 'image/png')


