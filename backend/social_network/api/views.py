from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.tokens import RefreshToken

from .filters import PostFilter
from .models import Post
from .permissions import IsAuthorOrAuthenticatedOnly
from .serializers import (PostSerializer, UserReadSerializer,
                          UserWriteSerializer)

User = get_user_model()


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user(request):
    user = get_object_or_404(User, username=request.user.username)
    return Response(UserReadSerializer(user).data)


@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    serializer = UserWriteSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.save()
    refresh = RefreshToken.for_user(user)
    user.is_active = True
    user.save()
    refresh = RefreshToken.for_user(user)
    return Response({'access': str(refresh.access_token)},
                    status=status.HTTP_201_CREATED)


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthorOrAuthenticatedOnly,)
    pagination_class = PageNumberPagination
    filter_backends = (DjangoFilterBackend,)
    filterset_class = PostFilter

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
