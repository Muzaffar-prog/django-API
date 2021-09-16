from django.urls import path
from .views import BookAPIview

urlpatterns = [
  path('', BookAPIview.as_view()),
]