
from django.urls import path
from .views import NewsListCreateAPIView,NewDetailAPIView

urlpatterns = [
    path('news/', NewsListCreateAPIView.as_view()),
    path('news/<int:pk>/', NewDetailAPIView.as_view()),
]

