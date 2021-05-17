from django.shortcuts import render
from rest_framework import generics, permissions
from .permissions import IsAuthorOrReadonly
from .models import Post
from .serializers import PostSerializer

# Create your views here.
# sainath
#sainath@3

class PostList(generics.ListCreateAPIView):
    # permission_classes = (permissions.IsAuthenticated,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadonly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer