from django.urls import path

from .views import home, index, PostListView, PostDetailView


urlpatterns = [
    path('', index, name='index'),
    path('home/', home, name='home'),
    # path('posts/', PostListView.as_view(), name='post_list'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
]
