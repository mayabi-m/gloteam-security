from django.urls import path
from . import views
app_name ='main'
urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.index, name="home"),
    path('about/', views.about, name="about"),
    path("service/", views.service, name='service'),
    path('guard/', views.guard, name="guard"),
    path('blog/', views.blog, name="blog"),
    path('single/', views.single, name="single"),
    path('contact/', views.contact, name="contact")
]