from django.urls import path
from . import views

app_name='blog'
urlpatterns = [
    path('', views.index_view, name='index'),
    path('post_list/', views.post_list, name='post_list'),
]