from rest_framework.generics import ListAPIView
from booksapp.models import Books
from .serializers import BookSerializers

class BookAPIview(ListAPIView):
  queryset = Books.objects.all()
  serializer_class = BookSerializers