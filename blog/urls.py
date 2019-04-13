from django.urls import path
from . import views

app_name='blog'
urlpatterns = [
    #path('', views.index_view, name='index'),
    #path('post_list/', views.post_list, name='post_list'),
    path('', views.IndexView.as_view(), name='index'),
    path('posts/<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('posts/', views.PostListView.as_view(), name='post_list'),
    path('about/', views.about_view, name='about'),
    path('contact/', views.contact_view, name='contact'),    
]