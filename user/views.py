from django.shortcuts import render_to_response

from models import User


def search(request):
    query = request.GET.get('q', '')
    if query:
        results = User.objects.filter(login__icontains=query)
        return render_to_response("html/user/search.html", {"results": results, "search": query})
    return render_to_response("html/user/search.html", {"results": [], "search": query})


def login(request):
    return render_to_response('html/user/login.html')


def menu(request):
    loginName = request.GET.get('login', '')
    password = request.GET.get('pass', '')
    if loginName:
        user = User.objects.get(login=loginName)
        if user.password == password:
            return render_to_response('html/menu.html', {"user": user})
    return render_to_response('html/menu.html', {"loginName": loginName})