from rest_framework import serializers
from booksapp.models import Books

class BookSerializers(serializers.ModelSerializer):
  class Meta:
    model = Books
    fields = ('title', 'subtitle', 'author', 'isbn')