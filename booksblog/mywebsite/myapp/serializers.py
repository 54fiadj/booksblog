from rest_framework import serializers
from .models import Book, Blog

class BookSerializer(serializers.ModelSerializer):
    picture = serializers.SerializerMethodField()

    def get_picture(self, book):
        request = self.context.get('request')
        if book.picture:
            return request.build_absolute_uri(book.picture.url)
        return None

    class Meta:
        model = Book
        fields = '__all__'

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'
