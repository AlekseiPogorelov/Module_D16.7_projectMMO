from django.contrib import admin

from .models import Post, UserResponse


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "subject",
        "user",
        "category",
    )
    list_display_links = ("subject",)
    list_filter = ("user", "category")


@admin.register(UserResponse)
class UserResponseAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "post",
        "subject",
    )
    list_display_links = ("subject",)
    list_filter = ("user",)
