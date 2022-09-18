from django.urls import path
from . import views



urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    # path('signup', views.Signup.as_view(), name = "signup"),

    path('posts/', views.PostList.as_view(), name="post"),
    path('posts/<int:pk>/', views.PostDetail.as_view(), name="post_detail"),
    path('posts/<int:pk>/update', views.PostUpdate.as_view(), name= "post_update"),
]