from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.conf import settings
from .models import Book, Blog
from .serializers import BookSerializer, BlogSerializer



def home(request):
    # Fetch necessary data from the database for home page
    # For example, get the latest book reviews and recent blog posts
    books = Book.objects.all()[:3]  # Limiting to 3 books for illustration
    blogs = Blog.objects.all()[:3]  # Limiting to 3 blogs for illustration

    return render(request, 'home.html', {'books': books, 'blogs': blogs})


def reviews(request):
    books = Book.objects.all()
    return render(request, 'reviews.html', {'books': books})

def blog(request):
    blogs = Blog.objects.all()
    return render(request, 'blog.html', {'blogs': blogs})

##

def get_base_url(request):
    return request.build_absolute_uri('/')

def get_books(request):
    # New API endpoint to fetch books data
    base_url = get_base_url(request)
    books = [{'id': book.id,
              'title': book.title,
              'author': book.author, 
              'review': book.review,
              'picture': base_url + settings.MEDIA_URL + str(book.picture) if book.picture else None,
              'rating': book.rating} for book in Book.objects.all()]
    return JsonResponse({'books': books})


def get_book_detail(request, pk):
    # API endpoint to fetch details of a single book
    book = get_object_or_404(Book, pk=pk)
    serializer = BookSerializer(book, context={'request': request})
    return JsonResponse(serializer.data)

def get_blogs(request):
    # New API endpoint to fetch blogs data
    blogs = [{'id': blog.id,
              'title': blog.title,
              'content': blog.content} for blog in Blog.objects.all()]
    return JsonResponse({'blogs': blogs})


def get_blog_detail(request, pk):
    # API endpoint to fetch details of a single blog
    blog = get_object_or_404(Blog, pk=pk)
    serializer = BlogSerializer(blog)

    return JsonResponse(serializer.data)