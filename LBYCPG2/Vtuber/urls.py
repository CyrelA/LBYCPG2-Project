from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostView.as_view(), name='index'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='about'),
    path('tags/<slug:tag_slug>/', views.TagView.as_view(), name='tags'),
    
]
