# from django.shortcuts import render
# from .serializers import NewsSerializer
# from rest_framework import generics
# from .models import News
#
# class NewsListCreateAPIView(generics.ListCreateAPIView):
#     serializer_class = NewsSerializer
#     queryset = News.objects.filter(is_archived=False)
#
# class NewDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = NewsSerializer
#     queryset = News.objects.all()


from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from .models import News
from .serializers import NewsSerializer

class NewsListCreateAPIView(ListCreateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

class NewsDetailAPIView(RetrieveAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer


