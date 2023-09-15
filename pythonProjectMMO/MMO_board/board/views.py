from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)
from django.urls import reverse_lazy

from .models import Post, UserResponse
from .form import PostForm, UserResponseForm


class PostList(ListView):
    model = Post
    queryset = Post.objects.all()
    template_name = "post_list.html"


class PostDetail(DetailView):
    model = Post
    queryset = Post.objects.all()
    context_object_name = "post"
    template_name = "post_detail.html"


class PostCreate(CreateView):
    form_class = PostForm
    model = Post
    template_name = "post_edit.html"


class PostUpdate(UpdateView):
    form_class = PostForm
    model = Post
    template_name = "post_edit.html"


class PostDelete(DeleteView):
    model = Post
    template_name = "post_delete.html"
    success_url = reverse_lazy('post-list')


class UserResponseList(ListView):
    model = UserResponse
    queryset = UserResponse.objects.all()
    template_name = "user_response_list.html"

    def get_queryset(self):
        return UserResponse.objects.filter(user=self.request.user)


class UserResponseCreate(CreateView):
    form_class = UserResponseForm
    model = UserResponse
    template_name = "user_respose_edit.html"
    success_url = reverse_lazy('post-list')


class SearchUserResponseList(ListView):
    model = UserResponse
    ordering = 'subject'
    template_name = 'user_response_search.html'
    context_object_name = 'posts'
    paginate_by = 20

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = UserResponseFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context
