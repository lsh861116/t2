from django.shortcuts import render, redirect

# Create your views here.
from django.shortcuts import HttpResponse
from django.shortcuts import render
from cmdb import models
from django.http import JsonResponse


user_list = [
    {"user":"jack", "pwd":"abc"},
{"user":"tom", "pwd":"ABC"},
]
def index(request):
    # return HttpResponse("hello world")
    # return render(request, "index.html")
    if request.method=='POST':
        username = request.POST.get("username", None)
        password = request.POST.get("password", None)
        models.UserInfo.objects.create(user=username,pwd=password)
    user_list=models.UserInfo.objects.all()
    return render(request, "register.html", {"data":user_list})

#name_dict = {'twz': 'Love python and Django', 'zqxt': 'I am teaching Django'}
    #return JsonResponse(name_dict)
def regiter(request):
    if request.method == 'POST':
        username = request.POST.get("username", None)
        password = request.POST.get("password", None)
        models.UserInfo.objects.create(user=username, pwd=password)
    return render(request, "index_v.html", {"data":username})

#logout
def login(request):
    if request.method == 'GET':
        return render(request, "register.htm")
    else:
        username = request.POST.get("username")
        password = request.POST.get("password")
        obj = models.UserInfo.objects.filter(username=username, password=password).first()
        if obj:
            request.session.session_key
            request.session['name']=obj.username
            request.session['email'] = 'zhanggen@le.com'
            return redirect('/index')
        else:
            return render(request,'register.html',{'msg':"用户名/密码错误"})
