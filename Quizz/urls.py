from django.urls import path, include, re_path

from . import views

from django.views.static import serve
from Pops_Quizz import settings
from django.conf.urls.static import static

app_name='Quizz'
urlpatterns = [

    path('', views.index, name='home'),
    path('users/', views.users, name='users'),
    path('creation/', views.creation, name='creation'),
    path('categories/', views.categories, name='categories'),
    path('resultats/', views.resultats, name='resultats'),
    path('create-game_<int:idform>/', views.resultats, name='create-game'),
    path('form_<int:idform>/', views.openform, name='openform'),

    re_path(r'create_user$', views.createUser),
    re_path(r'user_connection$', views.connectUser),


    re_path(r'^static/(?P<path>.*)$', serve,{'document_root':settings.STATIC_ROOT}),
]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)