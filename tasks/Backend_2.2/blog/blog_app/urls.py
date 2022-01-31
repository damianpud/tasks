from django.urls import path
from .views import PostUpdateView, PostDeleteView, PostDetailView, PostCreateView, AuthorPostListView

app_name = 'blog_app'

urlpatterns = [
    path('create', PostCreateView.as_view(), name='post_create'),
    path('update/<slug:slug>', PostUpdateView.as_view(), name='post_update'),
    path('delete/<slug:slug>', PostDeleteView.as_view(), name='post_delete'),
    path('detail/<slug:slug>', PostDetailView.as_view(), name='post_detail'),
    path('author_post_list', AuthorPostListView.as_view(), name='author_posts_list')
]
