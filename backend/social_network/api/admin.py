from django.contrib import admin
from django.contrib.auth import get_user_model

from .models import Post, PostImage

User = get_user_model()


class ImagesInlineAdmin(admin.TabularInline):
    model = PostImage


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'age', 'gender', 'about',
                    'register_date')
    search_fields = ('username',)
    list_filter = ('register_date',)
    empty_value_display = '-пусто-'


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('pk', 'author', 'text', 'pub_date',)
    search_fields = ('text',)
    list_filter = ('pub_date',)
    empty_value_display = '-пусто-'
    inlines = (ImagesInlineAdmin,)


@admin.register(PostImage)
class PostImageAdmin(admin.ModelAdmin):
    list_display = ('pk', 'post', 'image',)
    search_fields = ('post',)
