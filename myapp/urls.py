from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.index, name='home'),
    path("about", views.about, name='about'),
    path("services", views.services, name='services'),
    path("contact", views.contact, name='contact'),
    path("makeup", views.makeup, name='make up'),
    path("nail", views.nail, name='nail'),
    path("body_massage", views.body_massage, name='body massage'),
    path("skin_care", views.skin_care, name='skin care'),
    path("hair_care", views.hair_care, name='hair care'),
    path("hair_style", views.hair_style, name='hair style'),
]
