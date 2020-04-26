from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='havoc_home'),
    path('about/', views.about, name='havoc_about'),
    path('downloads/', views.downloads, name='havoc_downloads'),
    path('downloads/<slug:a_ver>', views.downloads, name='havoc_downloads_ver')
]