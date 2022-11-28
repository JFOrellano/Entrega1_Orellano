from django.urls import path

from home import views

app_name = "home"
urlpatterns = [
    path("", views.index, name="index"),
    path("search/", views.search, name="search"),
    path("about/", views.about, name="about"),
    path('login', views.login_request, name='login'),
    path('register', views.register, name='Register'),
    path('logout', LogoutView.as_views(template_name='home/logout.html'), name='logout'),
    path('editarPerfil',views.editarPerfil,name='EditarPerfil'),
]
