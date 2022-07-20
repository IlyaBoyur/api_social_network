from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Post, PostImage

User = get_user_model()


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    phone = PhoneNumberField()

    class Meta:
        model = User
        fields = ('phone', 'username', 'email', 'about',
                  'gender', 'age', 'register_date',)
