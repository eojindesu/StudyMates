from django.shortcuts import render, redirect
from .models import Join, jReply
from django.core.paginator import Paginator
from django.contrib import messages

# Create your views here.
def unjlikey(request, jpk):
    j = Join.objects.get(id=jpk)
    j.jlikey.remove(request.user)
    return redirect("join:detail", jpk)

def jlikey(request, jpk):
    j = Join.objects.get(id=jpk)
    j.jlikey.add(request.user)
    return redirect("join:detail", jpk)

def index(request):
    cate = request.GET.get("cate", "")
    kw = request.GET.get("kw", "")
    pg = request.GET.get("page", 1)

    if kw:
        if cate == "sub":
            j = Join.objects.filter(subject__startswith=kw)
        elif cate == "wri":
            try:
                from acc.models import User
                u = User.objects.get(username=kw)
                j = Join.objects.filter(jwriter=u)
            except:
                pass
        elif cate == "con":
            j = Join.objects.filter(content__contains=kw)
    else:
        j = Join.objects.all()

    pag = Paginator(j, 3)
    obj = pag.get_page(pg)
    context = {
        "jset" : obj,
        "cate" : cate,
        "kw" : kw,
    }
    return render(request, "join/index.html", context)

def detail(request, jpk):

    if request.user.is_anonymous:
        return redirect("acc:login")

    j = Join.objects.get(id=jpk)
    context = {
        "j" : j
    }
    return render(request, 'join/detail.html', context)

def delete(request, jpk):
    j = Join.objects.get(id=jpk)
    if j.jwriter == request.user:
        j.delete()
    else:
        messages.warning(request, "비정상적 접근입니다.")
    return redirect("join:index")

def create(request):
    if request.method == "POST":
        s = request.POST.get("sub")
        c = request.POST.get("con")
        Join(jsubject=s, jcontent=c, jwriter=request.user).save()
        return redirect("join:index")
    return render(request, "join/create.html")