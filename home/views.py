from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import *
from datetime import datetime, timedelta
from django.db.models import Avg
from django.shortcuts import redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import os
import pickle
import os


# Create your views here.
@login_required
def index2(request):
    now = datetime.now()
    current_year = now.year
    last = etat.objects.latest('id')

    with open('home/model.pickle', 'rb') as f:
        model = pickle.load(f)
    item = [[last.pressure,last.temperateur,last.flow,last.level,last.gas,last.vibration]]
    y_pred = model.predict(item)
    if y_pred[0] == 'Idle':   
        xmean = [825.8195,41.402,10.14,21,4.476,0.395]
        importances = model.feature_importances_
        result = [(float(x) - y)*z for x, y,z in zip(item[0], xmean,importances)]
        err = result.index(max(result))

    temp  =etat.objects.filter(year=current_year).values('mounth').annotate(avg_temp=Avg('temperateur'))
    temperateur = [0,0,0,0,0,0,0,0,0,0,0,0]

    for item in temp:
        temperateur[item['mounth'] - 1] = item['avg_temp']
    
    lev  =etat.objects.filter(year=current_year).values('mounth').annotate(avg_lev=Avg('level'))
    level = [0,0,0,0,0,0,0,0,0,0,0,0]

    for item in lev:
        level[item['mounth'] - 1] = item['avg_lev']

    ga  =etat.objects.filter(year=current_year).values('mounth').annotate(avg_gas=Avg('gas'))
    gas = [0,0,0,0,0,0,0,0,0,0,0,0]

    for item in ga:
        gas[item['mounth'] - 1] = item['avg_gas']

    pres  =etat.objects.filter(year=current_year).values('mounth').annotate(avg_pres=Avg('pressure'))
    pressure = [0,0,0,0,0,0,0,0,0,0,0,0]

    for item in pres:
        pressure[item['mounth'] - 1] = item['avg_pres']
        

    flo  =etat.objects.filter(year=current_year).values('mounth').annotate(avg_flo=Avg('flow'))
    flow = [0,0,0,0,0,0,0,0,0,0,0,0]

    for item in flo:
        flow[item['mounth'] - 1] = item['avg_flo']

    vib  =etat.objects.filter(year=current_year).values('mounth').annotate(avg_vib=Avg('vibration'))
    vibrating = [0,0,0,0,0,0,0,0,0,0,0,0]

    for item in vib:
        vibrating[item['mounth'] - 1] = item['avg_vib']



    context = {'last':last ,'pressure': pressure, 'temperateur':temperateur,'level':level,'flow':flow,'vibrating':vibrating,'gas':gas,'err':err}
    return render(request, 'pages/index.html',context)


@login_required
def index(request):
    now = datetime.now()
    current_year = now.year
    last = etat.objects.latest('id')

    with open('home/model.pickle', 'rb') as f:
        model = pickle.load(f)
    item = [[last.pressure,last.temperateur,last.flow,last.level,last.gas,last.vibration]]
    y_pred = model.predict(item)
    if y_pred[0] == 'Idle':   
        xmean = [825.8195,41.402,10.14,21,4.476,0.395]
        importances = model.feature_importances_
        result = [(float(x) - y)*z for x, y,z in zip(item[0], xmean,importances)]
        err = result.index(max(result))
        solut=solution.objects.values_list('solu', flat=True).get(prblm=err)
        

    temperateur  =percontage.objects.values_list('temperateur',flat=True).order_by('-id')[:10]
    pressure  =percontage.objects.values_list('pressure',flat=True).order_by('-id')[:10]
    level  =percontage.objects.values_list('level',flat=True).order_by('-id')[:10]
    flow  =percontage.objects.values_list('flow',flat=True).order_by('-id')[:10]
    vibrating  =percontage.objects.values_list('vibration',flat=True).order_by('-id')[:10]
    gas  =percontage.objects.values_list('gas',flat=True).order_by('-id')[:10]

   

    context = {'last':last ,'pressure': list(pressure), 'temperateur':list(temperateur),'level':list(level),'flow':list(flow),'vibrating':list(vibrating),'gas':list(gas),'err':err,'solu':solut}
    return render(request, 'pages/index.html',context)
 
#adding the current values
@csrf_exempt
def add(request):
 if request.method == "POST":
    now = datetime.now()
    current_month = now.month
    current_year = now.year
    context= request.POST 

    e = etat()
    e.mounth = current_month
    e.year = current_year
    e.temperateur=context.get('temperateur')
    e.level=context.get('level')
    e.flow=context.get('flow')
    e.gas=context.get('gas')
    e.vibration=context.get('vibration')
    e.pressure=context.get('pressure')
    e.save()
    with open('home/model.pickle', 'rb') as f:
        model = pickle.load(f)
    X = [context.get('pressure'),context.get('temperateur'),context.get('flow'),context.get('level'),context.get('gas'),context.get('vibration')]

    xmean = [825.8195,41.402,10.14,21,4.476,0.395]
    importances = model.feature_importances_
    
   
    result = [(float(x) - y)*z for x, y,z in zip(X, xmean,importances)]
    p = percontage()
    p.pressure = result[0]
    p.temperateur = result[1]
    p.flow= result[2]
    p.level = result[3]
    p.gas = result[4]
    p.vibration = result[5]
    p.save()

    return HttpResponse(context) 


@csrf_exempt
def addsolu(request):
 if request.method == "POST":
    context=request.POST
    s=solution()
    s.solu=context.get('solution')
    s.prblm=context.get('problem')
    s.save()
    return HttpResponse(context) 

