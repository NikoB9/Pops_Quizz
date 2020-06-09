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
    path('create-game-<int:id_form>/', views.create_game, name='create-game'),
    path('salle-attente/<str:game_uuid>/', views.attente, name='attente'),
    path('joindre-partie/<str:game_uuid>/', views.joindre_partie, name='joindre-partie'),
    path('quitter-partie/<str:game_uuid>/', views.quitter_partie, name='quitter-partie'),
    path('game/<str:game_uuid>/', views.openform, name='openform'),
    path('correction/<int:player_id>/', views.correction, name='correction'),
    path('resultats/<str:game_uuid>/', views.resultats, name='resultats'),
    path('show_cat_<int:cat_id>/', views.quizz_by_cat, name='show_cat'),
    path('edit_quizz_<int:id_quizz>/', views.edit_quizz, name='edit_quizz'),
    path('delete_quizz/<int:id_quizz>/', views.delete_quizz, name='delete_quizz'),
    path('edit_right/<int:id_quizz>/', views.edit_right, name='edit_right'),

    #DASHBOARD
    path('dashboard', views.user_profil, name="dashboard_base"),
    path('dashboard/user', views.user_profil, name="dashboard_profile"),
    path('dashboard/history', views.user_history, name="dashboard_history"),
    path('dashboard/classement', views.stats, name="dashboard_stats"),
    path('dashboard/amis', views.amis, name="dashboard_friend"),
    path('dashboard/game-progress', views.game_progress, name='dashboard-game-progress'),

    #Chat
    path('chat/', views.chat, name='chat'),
    path('chat/<str:room_name>/', views.room, name='room'),

    #AJAX
    re_path(r'create_user$', views.create_user, name="create_user"),
    re_path(r'user_connection$', views.connectUser, name="connectUser"),
    re_path(r'disconnect_user$', views.disconnect, name="disconnect"),
    re_path(r'save_user_answers$', views.saveUserAnswers, name="save_user_answers"),
    re_path(r'add_friend$', views.add_friend),
    re_path(r'remove_friend$', views.remove_friend),
    re_path(r'answer_friend_request$', views.answer_friend_request),
    re_path(r'change_user_invite$', views.change_user_invite),
    re_path(r'categories_menu$', views.menuCategories, name="menuCategories"),
    re_path(r'invite_friend$', views.invite_friend),
    re_path(r'kick_user$', views.kick_user),
    re_path(r'refuse_game_invitation$', views.refuse_game_invitation),
    re_path(r'question_answer_by$', views.question_answer_by),


    re_path(r'^static/(?P<path>.*)$', serve,{'document_root':settings.STATIC_ROOT}),
]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
