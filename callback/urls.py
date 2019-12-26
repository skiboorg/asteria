from django.urls import path
from . import views

urlpatterns = [

   path('callback/', views.createCallbackForm, name='createCallbackForm'),
   path('quiz/', views.createQuiz, name='createQuiz'),


]
