from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='itreporting'),
    path('', views.about, name='itreporting'),
] 