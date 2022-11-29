from django.urls import path
from django.contrib.auth.views import LogoutView
from home import views
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy


app_name = "home"
urlpatterns = [
    path("", views.index, name="index"),
    path("search/", views.search, name="search"),
    path("about/", views.about, name="about"),
    path('login', views.login_request, name='login'),
<<<<<<< HEAD
#    path('registracion', views.registracion, name='Register'),
=======
    path('registracion', views.register, name='Register'),
>>>>>>> 0dba04d436131733b5081eafe74e04fe290d9c9d
    path('logout', LogoutView.as_view(template_name='home/logout.html'), name='logout'),
    path('editarPerfil',views.editarPerfil,name='EditarPerfil'),
#    path('registracion/update/', views.user_update, name='user-update'),
    path(
        'password_change/',
        auth_views.PasswordChangeView.as_view(
            template_name='registration/change-password.html',
            success_url=reverse_lazy("home:password-change-done")
        ),
        name="password-change"
    ),
    path(
        'password_change/done/',
        auth_views.PasswordChangeDoneView.as_view(
            template_name='registration/change-password-done.html'
        ),
        name="password-change-done"
    ),
]
