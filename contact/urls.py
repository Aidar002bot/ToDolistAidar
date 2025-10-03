from django.urls import path
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Contact

urlpatterns = [
    path('', ListView.as_view(model=Contact), name='contact_list'),
    path('<int:pk>/', DetailView.as_view(model=Contact), name='contact_detail'),
    path('create/', CreateView.as_view(model=Contact, fields="__all__",
         success_url="/contact/"), name='contact_create'),
    path('<int:pk>/update/', UpdateView.as_view(model=Contact, fields="__all__",
         success_url="/contact/"), name='contact_update'),
    path('<int:pk>/delete/', DeleteView.as_view(model=Contact,
         success_url="/contact/"), name='contact_delete'),
]