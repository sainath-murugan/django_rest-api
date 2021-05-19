from django.contrib.auth import get_user_model
from rest_framework import generics, permissions, serializers, viewsets
from .permissions import IsAuthorOrReadonly
from .models import Post
from .serializers import PostSerializer, UserSerializer

# Create your views here.
# sainath
#sainath@3

class PostViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthorOrReadonly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

