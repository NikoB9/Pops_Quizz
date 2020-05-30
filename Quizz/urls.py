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
    path('resultats/<str:game_uuid>/', views.resultats, name='resultats'),
    path('game/<int:id_form>/', views.openform, name='openform'),
    path('create-game-<int:id_form>/', views.create_game, name='create-game'),
    path('correction/<int:player_id>/', views.correction, name='correction'),
    path('show_cat_<int:cat_id>/', views.quizz_by_cat, name='show_cat'),
    path('edit_quizz_<int:id_quizz>/', views.edit_quizz, name='edit_quizz'),

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