from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import Item
from django.urls import reverse_lazy  # new
from .forms import ItemForm


class HomePageView(ListView):
    model = Item
    template_name = "home.html"


class ItemCreateView(CreateView):
    model = Item
    form_class = ItemForm
    template_name = "item.html"
    success_url = reverse_lazy('home')
