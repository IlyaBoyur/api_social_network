from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Post, User
from .serializers import PostSerializer, UserSerializer


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user(request):
    user = get_object_or_404(User, username=request.user.username)
    return Response(UserSerializer(user).data)


@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    serializer = UserSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.save()
    refresh = RefreshToken.for_user(user)
    user.is_active = True
    user.save()
    return Response({'token': str(refresh.access_token)},
                    status=status.HTTP_200_OK)


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
