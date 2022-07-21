from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .fields import Base64ImageField, PhoneNumberField
from .models import Post, PostImage
from .settings import POST_IMAGES_MAX_SIZE
from .validators import MaxSizeValidator

ERROR_MAX_IMAGE_SIZE = (
    'Превышен размер изображений для поста: {size} > {max_size}'
)

User = get_user_model()


class PostImageSerializer(serializers.ModelSerializer):
    image = Base64ImageField()

    class Meta:
        model = PostImage
        fields = ('image',)


class PostSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(slug_field='username',
                                          read_only=True)
    images = PostImageSerializer(many=True,
                                 allow_empty=False)

    class Meta:
        model = Post
        fields = '__all__'
        validators = (
            MaxSizeValidator('images',
                             'image',
                             max_size=POST_IMAGES_MAX_SIZE,
                             message=ERROR_MAX_IMAGE_SIZE),
        )

    def create(self, validated_data):
        post = Post.objects.create(
            **{field: value
               for field, value in validated_data.items()
               if field not in ('images',)}
        )
        self.update_images(post, validated_data)
        return post

    def update(self, instance, validated_data):
        self.update_images(instance, validated_data)
        return super().update(
            instance,
            {key: value
             for key, value in validated_data.items()
             if key not in ('images',)},
        )

    def update_images(self, instance, validated_data):
        images = validated_data.get('images')
        if images is not None:
            instance.images.all().delete()
            PostImage.objects.bulk_create(
                PostImage(image=image['image'], post_id=instance.id)
                for image in images
            )


class UserWriteSerializer(serializers.ModelSerializer):
    phone = PhoneNumberField(
        validators=(UniqueValidator(queryset=User.objects.all()),),
    )

    class Meta:
        model = User
        fields = ('phone', 'username', 'email', 'password', 'about',
                  'gender', 'age',)


class UserReadSerializer(serializers.ModelSerializer):
    phone = PhoneNumberField(
        validators=(UniqueValidator(queryset=User.objects.all()),),
    )

    class Meta:
        model = User
        fields = ('id', 'phone', 'username', 'email', 'about',
                  'gender', 'age', 'register_date',)
