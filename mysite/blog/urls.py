from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='blog-index'),
    path('about/', views.aboutPage, name='blog-about'),
    path('contact/', views.aboutContact, name='blog-contact'),
    path('posts/', views.posts, name='blog-posts'),
    path('posts/create/', views.createPost, name='blog-createpost'),
    path('register/', views.registerPage, name='blog-register'),
    path('login/', views.loginPage, name='blog-login'),
    path('logout/', views.logoutUser, name='blog-logout')
]