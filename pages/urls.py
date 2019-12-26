from django.urls import path
from . import views
from django.views.generic.base import RedirectView

urlpatterns = [

   path('', views.index, name='index'),
   path('index.html', RedirectView.as_view(url='/', permanent=False), name='index1'),
   path('index.php', RedirectView.as_view(url='/', permanent=False), name='index2'),
   path('service/<slug>/', views.service, name='service'),
   path('robots.txt', views.robots, name='robots'),



]
