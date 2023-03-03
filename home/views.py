from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import *
from datetime import datetime, timedelta
from django.db.models import Avg
from django.shortcuts import redirect



# Create your views here.
@login_required
def index(request):
    now = datetime.now()
    current_year = now.year
    last = etat.objects.latest('id')
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
        print(item)

    flo  =etat.objects.filter(year=current_year).values('mounth').annotate(avg_flo=Avg('flow'))
    flow = [0,0,0,0,0,0,0,0,0,0,0,0]

    for item in flo:
        flow[item['mounth'] - 1] = item['avg_flo']

    vib  =etat.objects.filter(year=current_year).values('mounth').annotate(avg_vib=Avg('vibration'))
    vibrating = [0,0,0,0,0,0,0,0,0,0,0,0]

    for item in vib:
        vibrating[item['mounth'] - 1] = item['avg_vib']



    context = {'last':last ,'pressure': pressure, 'temperateur':temperateur,'level':level,'flow':flow,'vibrating':vibrating,'gas':gas}
    return render(request, 'pages/index.html',context)
 

def add(request):
 if request.method == "POST":
    now = datetime.now()
    current_month = now.month
    current_year = now.year
    e = etat()
    e.temperateur = request.data['temperateur']
    e.level = request.data['level']
    e.flow = request.data['flow']
    e.gas = request.data['gas']
    e.vibration = request.data['vibration']
    e.pressure = request.data['pressure']
    e.mounth = current_month
    e.year = current_year
    e.save()
    return e