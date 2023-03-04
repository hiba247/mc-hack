from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('detail/', views.index2, name='index2'),
    path('add/',views.add , name='add'),
    path('addsolu/',views.addsolu , name='add')

]
