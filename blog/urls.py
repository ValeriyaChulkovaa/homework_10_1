from django.urls import path
from blog.apps import BlogConfig

from blog.views import BlogListView, BlogCreateView, BlogUpdateView, BlogDeleteView, BlogDetailView

app_name = BlogConfig.name

urlpatterns = [
    path('', BlogListView.as_view(), name='index'),
    path('add_post/', BlogCreateView.as_view(), name='add_post'),
    path('detail/<int:pk>/', BlogDetailView.as_view(), name='blog_detail'),
    path('edit_post/<int:pk>/', BlogUpdateView.as_view(), name='edit_post'),
    path('delete_post/<int:pk>/', BlogDeleteView.as_view(), name='delete_post'),
]