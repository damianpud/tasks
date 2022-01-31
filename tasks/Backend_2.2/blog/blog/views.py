from blog_app.views import PostListView


class IndexView(PostListView):
    title = 'Welcome to Blog!'
    template_name = 'index.html'
