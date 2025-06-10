from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from .models import Blog
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from .forms import BlogForm


class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Blog
    # fields = ['title', 'content', 'preview']
    form_class = BlogForm
    template_name = 'blog/add_post.html'

    def get_success_url(self):
        return f'/blog/detail/{self.object.pk}/'


class BlogListView(ListView):
    model = Blog
    template_name = 'blog/index.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Blog.objects.filter(is_published=True)


class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blog/detail.html'
    context_object_name = 'post'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        obj.views_count += 1
        obj.save(update_fields=['views_count'])
        return obj


class BlogUpdateView(LoginRequiredMixin, UpdateView):
    model = Blog
    form_class = BlogForm
    template_name = 'blog/edit_post.html'
    context_object_name = 'post'

    def get_success_url(self):
        return f'/blog/detail/{self.object.pk}/'


class BlogDeleteView(LoginRequiredMixin, DeleteView):
    model = Blog
    template_name = 'blog/delete_post.html'
    success_url = reverse_lazy('blog:index')
    context_object_name = 'post'