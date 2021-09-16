from django.db import models
from django.shortcuts import render
from django.views.generic import ListView
from .models import Books

class BookListView(ListView):
  model = Books
  template_name = 'book_list.html'
  context_object_name = 'kitoblar'