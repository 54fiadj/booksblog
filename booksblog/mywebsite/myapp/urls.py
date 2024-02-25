from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('reviews/', views.reviews, name='reviews'),
    path('blog/', views.blog, name='blog'),
    
    path('api/books/', views.get_books, name='get_books'),
    path('api/books/<int:pk>/', views.get_book_detail, name='get_book_detail'),
    path('api/blogs/', views.get_blogs, name='get_blogs'),
    path('api/blogs/<int:pk>/', views.get_blog_detail, name='get_blog_detail'),
]
