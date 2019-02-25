#  -*- coding: UTF-8 -*-
from bravado.exception import HTTPForbidden
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect, Http404, HttpResponse, HttpResponseForbidden
from django.shortcuts import render
from django.utils.baseconv import base62


import models as database
import ujson as json
__author__ = 'copyliu'


def default(request,ID):
    return render(request,'default.html')

def postnew(request,ID):
    if request.method=='POST':

        pk = base62.decode(ID)
        try:
            box=database.BoxModel.objects.get(user_id=pk)
        except:
            raise Http404
        model=database.Asks()
        model.box=box
        model.body=request.POST.get('t','')
        model.save()

    return HttpResponseRedirect('.')

@login_required
def admin_page(request,ID):
    pk = base62.decode(ID)
    if request.user.pk!=pk:
        return HttpResponseForbidden(request)
    return render(request,'admin.html')
@login_required
def admin_list(request,ID):
    pk = base62.decode(ID)
    if request.user.pk!=pk:
        return HttpResponseForbidden(request)
    query=database.Asks.objects.filter(box_id=ID).all()
    result=[]
    for i in query:
        result.append({"body":i.body})
    return HttpResponse(content=json.dumps(result),content_type='application/json')




@login_required
def admin_delete(request,ID):
    pk = base62.decode(ID)
    if request.user.pk!=pk:
        return HttpResponseForbidden(request)
    pass
@login_required
def admin_read(request,ID):
    pk = base62.decode(ID)
    if request.user.pk!=pk:
        return HttpResponseForbidden(request)
    pass

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            new_user2 = database.BoxModel()
            new_user2.user=new_user
            new_user2.save()
            return HttpResponseRedirect("/login/")
    else:
        form = UserCreationForm()
    return render(request,"registration/register.jinja", {
        'form': form,
    })

