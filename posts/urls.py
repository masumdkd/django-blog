from django.urls import path
from . import views
from .views import HomeView, PostView, AddPostView, UpdatePostView, DeleteViewPost

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('post/<int:pk>', PostView.as_view(), name="post" ), 
    path('post/add', AddPostView.as_view(), name="add_post" ), 
    path('post/edit/<int:pk>', UpdatePostView.as_view(), name="update_post" ), 
    path('post/<int:pk>/remove', DeleteViewPost.as_view(), name="delete_post" ), 
]


