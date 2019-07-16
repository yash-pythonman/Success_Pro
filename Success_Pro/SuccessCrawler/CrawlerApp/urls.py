from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('crawler/', views.Crawler.as_view(), name="crawler"),
    path('image/', views.image_view, name='image'),
    #path('crawler/', views.crawler, name='crawler')

]
