from django.urls import path
from .views import PostListView, PostDetailView

urlpatterns = [
    path('posts/', PostListView.as_view()),
    path('posts/&lt;int:pk&gt;', PostDetailView.as_view()),
]