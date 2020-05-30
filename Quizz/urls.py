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
    path('create-game-<int:id_form>/', views.create_game, name='create-game'),
    path('salle-attente/<str:game_uuid>/', views.attente, name='attente'),
    path('game/<str:game_uuid>/', views.openform, name='openform'),
    path('correction/<int:player_id>/', views.correction, name='correction'),
    path('resultats/<str:game_uuid>/', views.resultats, name='resultats'),
    path('show_cat_<int:cat_id>/', views.quizz_by_cat, name='show_cat'),



    #DASHBOARD
    path('dashboard/user', views.user_profil, name="dashboard_profile"),
    path('dashboard/history', views.user_history, name="dashboard_history"),

    #AJAX
    re_path(r'create_user$', views.create_user),
    re_path(r'user_connection$', views.connectUser),
    re_path(r'disconnect_user$', views.disconnect),
    re_path(r'save_user_answers$', views.saveUserAnswers),
    re_path(r'categories_menu$', views.menuCategories),


    re_path(r'^static/(?P<path>.*)$', serve,{'document_root':settings.STATIC_ROOT}),
]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)