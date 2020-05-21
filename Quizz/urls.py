from django.urls import path, include, re_path

from . import views

from django.views.static import serve
from Pops_Quizz import settings
from django.conf.urls.static import static

app_name='Quizz'
urlpatterns = [

    path('', views.index, name='home'),
    path('users/', views.users, name='users'),
    path('forms/', views.getforms, name='forms'),
    path('oneform/', views.openform, name='oneform'),
    path('createUser/', views.createUser, name='createUser'),
    path('creation/', views.creation, name='creation'),
    path('categories/', views.categories, name='categories'),
    path('resultats/', views.resultats, name='resultats'),


    re_path(r'^static/(?P<path>.*)$', serve,{'document_root':settings.STATIC_ROOT}),
]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)