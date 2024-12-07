from rest_framework import generics
from .models import Blog
from .serializers import BlogSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated , IsAdminUser
from rest_framework.exceptions import NotFound
from markdown import markdown
from django.shortcuts import render, get_object_or_404




# Create your views here.


class BlogListView(generics.ListAPIView):
    serializer_class = BlogSerializer
    queryset = Blog.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly] 

class BlogDetailView(generics.RetrieveAPIView):
    serializer_class = BlogSerializer
    queryset = Blog.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly] 
    lookup_field = 'slug'


class BlogCreateView(generics.CreateAPIView):
    serializer_class = BlogSerializer
    queryset = Blog.objects.all()
    permission_classes = [IsAdminUser]


class BlogUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BlogSerializer
    queryset = Blog.objects.all()
    permission_classes = [IsAdminUser]
    lookup_field = 'slug'
    def get_object(self):
        slug = self.kwargs.get('slug')
        try:
            return Blog.objects.get(slug=slug)
        except Blog.DoesNotExist:
            raise NotFound(detail="Blog with the specified slug does not exist.")
        
        