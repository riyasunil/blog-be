from django.urls import path
from .views import BlogListView, BlogDetailView, BlogCreateView, BlogUpdateDeleteView
urlpatterns = [
    path('blogs/', BlogListView.as_view(),name='Blog-list' ),
    path('blogs/<slug:slug>/', BlogDetailView.as_view(), name='Blog-detail'),
    path('blogs/manage/<slug:slug>/', BlogUpdateDeleteView.as_view(), name='blog-manage'), 
    path('blogs/create/', BlogCreateView.as_view(), name='blog-create'), 
]
