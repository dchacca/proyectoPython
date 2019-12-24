from django.urls import path
from .views import HomePageView, ItemCreateView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("item/", ItemCreateView.as_view(), name="add_item")
]
