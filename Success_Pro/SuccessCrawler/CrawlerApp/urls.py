from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('crawler/', views.Crawler.as_view(), name="crawler"),
    #path('frontend/', views.BaseUrlView, name= 'frontend'),
    #path('crawler/', views.crawler, name='crawler')
    # path('image/', views.image_view, name='image'),
    #path('apicrawler/', views.UrlDepthView.as_view(), name="apicrawler"),
    path('apicrawler/',    views.UrlDepthView, name="apicrawler"),
    path('homepageimages/' , views.BaseUrlImageView.as_view(), name ='homepageimage'),
    path('subpageimages/', views.PageImagesView.as_view(), name='pageimage'),
    path('basepageurls/', views.BaseUrlView, name='baseurl'),
    path('subpageurls/', views.PageUrlView.as_view(), name='pageimage')

]
