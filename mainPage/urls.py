from django.urls import path
from .views import PostDetailView, PostListView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView
from . import views
urlpatterns = [
    path('', PostListView.as_view(), name='mainPage-home'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='mainPage-about'),
    path('store/', views.store, name='mainPage-store'),
    path('obituary/', views.obituary, name='mainPage-obituary'),
    path('emergency/', views.emergency, name='mainPage-emergency'),
    path('training/', views.training, name='mainPage-training'),
]