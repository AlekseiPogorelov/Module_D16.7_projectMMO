from django_filters import FilterSet

from board.models import UserResponse


class UserResponseFilter(FilterSet):
    class Meta:
        model = UserResponse
        fields = {'post': ['exact'], }