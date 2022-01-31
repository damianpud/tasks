from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from blog.mixins import TitleMixin, SuccessMessagedFormMixin
from django.urls import reverse_lazy
from django.contrib import messages
from django.utils.html import escape
from django.utils.safestring import SafeString
from django.utils.text import slugify

from .models import Post
from .forms import PostForm


class PostListView(TitleMixin, ListView):
    title = 'Post list'
    template_name = 'post_list.html'
    model = Post
    paginate_by = 30


class AuthorPostListView(TitleMixin, ListView):
    model = Post
    title = 'Your posts'
    template_name = 'post_list.html'
    paginate_by = 30

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(author=self.request.user)


class PostDetailView(TitleMixin, DetailView):
    template_name = 'post_detail.html'
    model = Post


class PostCreateView(TitleMixin,
                     SuccessMessagedFormMixin,
                     LoginRequiredMixin,
                     CreateView):
    template_name = 'form.html'
    title = 'Create post'
    form_class = PostForm
    success_url = reverse_lazy('index')
    permission_required = 'blog_app.add_post'

    def get_success_message(self):
        safe_title = escape(self.object.title)
        return SafeString(f'Post <strong>{safe_title} </strong> added!')

    def form_valid(self, form):
        post = form.save(commit=False)
        post.author = self.request.user
        post.save()
        post.slug = slugify(str(f'{post.pk}-') + post.title)
        post.save()
        return super().form_valid(form)


class PostUpdateView(TitleMixin,
                     SuccessMessagedFormMixin,
                     LoginRequiredMixin,
                     UpdateView):
    title = 'Update post'
    model = Post
    permission_required = 'blog_app.change_post'
    template_name = 'form.html'
    form_class = PostForm
    success_url = reverse_lazy('index')

    def get_success_message(self):
        safe_title = escape(self.object.title)
        return SafeString(f'Post <strong>{safe_title}</strong> updated!')

    def form_valid(self, form):
        post = form.save(commit=False)
        post.slug = slugify(str(f'{post.slug}-') + post.title)
        post.save()
        return super().form_valid(form)


class PostDeleteView(TitleMixin,
                     LoginRequiredMixin,
                     DeleteView):
    title = 'Confirm delete post'
    template_name = 'post_confirm_delete.html'
    model = Post
    success_url = reverse_lazy('index')
    permission_required = 'blog_app.delete_post'

    def get_title(self):
        safe_title = escape(self.object.title)
        return SafeString(f'Delete <em>{safe_title}</em>')

    def post(self, request, *args, **kwargs):
        result = super().post(request, *args, **kwargs)
        safe_title = escape(self.object.title)
        message = SafeString(f'Post <strong>{safe_title}</strong> removed.')
        messages.success(request, message)
        return result

